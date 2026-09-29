#!/usr/bin/env python3
"""
EMS Controller Web App - Flask Backend with BLE Support
Self-contained cross-platform web app for controlling EMS device via BLE
"""

import os
import sys
import json
import asyncio
import threading

# On Windows, keep WinRT/Bleak on the MTA threading model. This avoids common
# "callbacks are not working" hangs when a package initializes COM as STA.
if sys.platform == "win32":
    sys.coinit_flags = 0

from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from bleak import BleakClient, BleakScanner
import logging

app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# BLE Configuration
APP_VERSION = "2026-06-25-win-ble-notify-fix"
SERVICE_UUID = "6E400001-B5A3-F393-E0A9-E50E24DCCA9E"
RX_UUID = "6E400002-B5A3-F393-E0A9-E50E24DCCA9E"
TX_UUID = "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"
TARGET_NAME = "EMS Controller"
BLE_SCAN_TIMEOUT_SEC = 10.0
BLE_CONNECT_TIMEOUT_SEC = 15.0
BLE_NOTIFY_TIMEOUT_SEC = 10.0
BLE_ROUTE_TIMEOUT_SEC = 30.0

# Global state
ble_client = None
ble_device = None
device_connected = False
last_ble_error = None
ble_loop = None
ble_loop_thread = None
message_callbacks = []
app_dir = os.path.dirname(os.path.abspath(__file__))
config_dir = os.path.join(app_dir, "configurations")

# Ensure config directory exists
os.makedirs(config_dir, exist_ok=True)

logger.info("EMS web app backend version: %s", APP_VERSION)
logger.info("EMS web app backend file: %s", os.path.abspath(__file__))
logger.info("EMS web app config directory: %s", config_dir)


def notify_listeners(message):
    """Broadcast message to all connected websocket listeners"""
    for callback in message_callbacks:
        try:
            callback(message)
        except:
            pass


def on_disconnect(client):
    """Called when BLE device disconnects"""
    global device_connected, ble_client
    if ble_client is not None and ble_client is not client:
        logger.info("Ignoring disconnect callback from stale BLE client")
        return

    device_connected = False
    ble_client = None
    notify_listeners({"type": "disconnected", "message": "Device disconnected"})
    logger.info("BLE device disconnected")


def is_ble_connected():
    """Return the real BLE connection state and clear stale cached state."""
    global device_connected, ble_client

    connected = bool(ble_client and getattr(ble_client, "is_connected", False))
    if not connected:
        device_connected = False
        ble_client = None
    else:
        device_connected = True
    return device_connected


def start_ble_loop():
    """Start one persistent asyncio loop for all BLE work."""
    global ble_loop, ble_loop_thread

    if ble_loop and ble_loop.is_running():
        return

    ble_loop = asyncio.new_event_loop()

    def run_loop():
        asyncio.set_event_loop(ble_loop)
        ble_loop.run_forever()

    ble_loop_thread = threading.Thread(target=run_loop, name="BLEEventLoop", daemon=True)
    ble_loop_thread.start()


async def handle_ble_messages(client):
    """Handle incoming BLE messages"""
    if client is None:
        raise RuntimeError("BLE client disappeared before notify setup")
    if not getattr(client, "is_connected", False):
        raise RuntimeError("BLE client disconnected before notify setup")

    async def callback(sender, data):
        message = data.decode('utf-8', errors='ignore').strip()
        if message:
            notify_listeners({"type": "message", "data": message})
            logger.info(f"RX: {message}")
    
    logger.info("Starting notify on TX characteristic %s", TX_UUID)
    await asyncio.wait_for(
        client.start_notify(TX_UUID, callback),
        timeout=BLE_NOTIFY_TIMEOUT_SEC,
    )
    logger.info("Notify started on TX characteristic")


def device_matches_target(device, advertisement_data=None):
    """Return True when a discovered BLE device looks like the EMS controller."""
    device_name = getattr(device, "name", None)
    if advertisement_data and getattr(advertisement_data, "local_name", None):
        device_name = advertisement_data.local_name

    service_uuids = []
    if advertisement_data:
        service_uuids = getattr(advertisement_data, "service_uuids", None) or []
    if not service_uuids:
        metadata = getattr(device, "metadata", None) or {}
        service_uuids = metadata.get("uuids", []) or []

    return (
        device_name == TARGET_NAME
        or SERVICE_UUID.lower() in [str(uuid).lower() for uuid in service_uuids]
    )


def describe_device(device, advertisement_data=None):
    """Return a compact debug description for scan results."""
    device_name = getattr(device, "name", None) or "(no name)"
    local_name = getattr(advertisement_data, "local_name", None) if advertisement_data else None
    address = getattr(device, "address", None) or "(no address)"
    service_uuids = getattr(advertisement_data, "service_uuids", None) if advertisement_data else None
    return f"name={device_name}, local_name={local_name}, address={address}, uuids={service_uuids or []}"


async def discover_target_device():
    """Find the EMS controller using both modern and older Bleak APIs."""
    try:
        discovered = await BleakScanner.discover(timeout=BLE_SCAN_TIMEOUT_SEC, return_adv=True)
        logger.info("BLE scan found %d devices", len(discovered))
        for device, advertisement_data in discovered.values():
            logger.info("BLE device: %s", describe_device(device, advertisement_data))
            if device_matches_target(device, advertisement_data):
                return device
    except TypeError:
        # Older Bleak versions do not support return_adv.
        devices = await BleakScanner.discover(timeout=BLE_SCAN_TIMEOUT_SEC)
        logger.info("BLE scan found %d devices", len(devices))
        for device in devices:
            logger.info("BLE device: %s", describe_device(device))
            if device_matches_target(device):
                return device

    return None


async def ble_scan_and_connect():
    """Scan for EMS Controller device and connect"""
    global ble_client, ble_device, device_connected, last_ble_error
    client = None
    connection_step = "starting"
    
    try:
        last_ble_error = None
        device_connected = False
        ble_client = None

        logger.info("Starting BLE scan...")
        notify_listeners({"type": "status", "message": "Scanning for EMS Controller..."})
        
        # Scan for devices
        connection_step = "scanning"
        target = await discover_target_device()
        
        if not target:
            last_ble_error = f"Device '{TARGET_NAME}' not found during BLE scan"
            notify_listeners({"type": "error", "message": last_ble_error})
            logger.warning(last_ble_error)
            return False
        
        logger.info(f"Found device: {target.name} ({target.address})")
        notify_listeners({"type": "status", "message": f"Connecting to {target.name}..."})
        
        # Connect
        connection_step = "connecting"
        client = BleakClient(target, disconnected_callback=on_disconnect)
        logger.info("Connecting to BLE device...")
        await asyncio.wait_for(client.connect(), timeout=BLE_CONNECT_TIMEOUT_SEC)
        if not getattr(client, "is_connected", False):
            raise RuntimeError("BLE connect returned but client is not connected")
        logger.info("BLE link connected; enabling notify")

        # Start listening for messages before reporting success. If this fails,
        # the app must remain disconnected so commands are not sent into a
        # half-open Windows BLE connection.
        connection_step = "enabling notify"
        await handle_ble_messages(client)

        connection_step = "connected"
        ble_client = client
        ble_device = target.address
        device_connected = True
        
        logger.info("Connected successfully; notify enabled")
        notify_listeners({"type": "connected", "message": f"Connected to {target.name}"})

        return True
        
    except Exception as e:
        detail = str(e) or f"{connection_step} timed out or failed"
        last_ble_error = f"{type(e).__name__} during {connection_step}: {detail}"
        logger.exception("BLE connection error")
        notify_listeners({"type": "error", "message": f"Connection error: {last_ble_error}"})
        device_connected = False
        ble_client = None
        try:
            if client and getattr(client, "is_connected", False):
                await client.disconnect()
        except Exception:
            logger.exception("Error while cleaning up failed BLE connection")
        return False


async def ble_send_command(command):
    """Send command to EMS device via BLE"""
    global ble_client
    
    if not ble_client or not device_connected:
        return False
    
    try:
        msg = (command + "\n").encode('utf-8')
        await ble_client.write_gatt_char(RX_UUID, msg)
        logger.info(f"TX: {command}")
        return True
    except Exception as e:
        logger.error(f"Error sending command: {e}")
        return False


def run_ble_async(coroutine):
    """Run async BLE operations on the persistent BLE event loop."""
    start_ble_loop()
    future = asyncio.run_coroutine_threadsafe(coroutine, ble_loop)
    try:
        return future.result(timeout=BLE_ROUTE_TIMEOUT_SEC)
    except TimeoutError:
        future.cancel()
        raise TimeoutError(f"BLE operation timed out after {BLE_ROUTE_TIMEOUT_SEC:.0f} seconds")
    except Exception:
        future.cancel()
        raise


# ============ Flask Routes ============

@app.route('/')
def index():
    """Serve main page"""
    return render_template('index.html')


@app.route('/api/scan', methods=['POST'])
def api_scan():
    """Scan and connect to BLE device"""
    try:
        if is_ble_connected():
            return jsonify({"success": True})
        result = run_ble_async(ble_scan_and_connect())
        if result:
            return jsonify({"success": True})
        error = last_ble_error or "BLE scan/connect failed without a detailed error; check the Flask console log"
        return jsonify({"success": False, "error": error})
    except Exception as e:
        logger.exception("Scan error")
        return jsonify({"success": False, "error": f"{type(e).__name__}: {e}"})


@app.route('/api/disconnect', methods=['POST'])
def api_disconnect():
    """Disconnect from BLE device"""
    global ble_client, device_connected
    client = ble_client
    device_connected = False
    ble_client = None

    try:
        if client and getattr(client, "is_connected", False):
            run_ble_async(client.disconnect())
        notify_listeners({"type": "disconnected", "message": "Disconnected"})
        return jsonify({"success": True})
    except Exception as e:
        logger.error(f"Disconnect error: {e}")
        return jsonify({"success": False, "error": str(e)})


@app.route('/api/send', methods=['POST'])
def api_send():
    """Send command to device"""
    data = request.get_json()
    command = data.get('command', '').strip()
    
    if not command:
        return jsonify({"success": False, "error": "Empty command"})
    
    try:
        result = run_ble_async(ble_send_command(command))
        return jsonify({"success": result})
    except Exception as e:
        logger.error(f"Send error: {e}")
        return jsonify({"success": False, "error": str(e)})


@app.route('/api/status', methods=['GET'])
def api_status():
    """Get connection status"""
    return jsonify({
        "connected": is_ble_connected(),
        "device": ble_device
    })


@app.route('/api/config/save', methods=['POST'])
def api_config_save():
    """Save configuration to file"""
    data = request.get_json()
    config_name = data.get('name', 'default').replace('/', '_').replace('\\', '_')
    
    if not config_name:
        return jsonify({"success": False, "error": "Config name required"})
    
    try:
        config_path = os.path.join(config_dir, f"{config_name}.json")
        with open(config_path, 'w') as f:
            json.dump(data.get('config', {}), f, indent=2)
        return jsonify({"success": True, "message": f"Config saved as '{config_name}'"})
    except Exception as e:
        logger.error(f"Config save error: {e}")
        return jsonify({"success": False, "error": str(e)})


@app.route('/api/config/load/<config_name>', methods=['GET'])
def api_config_load(config_name):
    """Load configuration from file"""
    try:
        config_path = os.path.join(config_dir, f"{config_name}.json")
        if not os.path.exists(config_path):
            return jsonify({"success": False, "error": "Config not found"})
        
        with open(config_path, 'r') as f:
            config = json.load(f)
        return jsonify({"success": True, "config": config})
    except Exception as e:
        logger.error(f"Config load error: {e}")
        return jsonify({"success": False, "error": str(e)})


@app.route('/api/config/list', methods=['GET'])
def api_config_list():
    """List all saved configurations"""
    try:
        configs = []
        if os.path.exists(config_dir):
            for filename in os.listdir(config_dir):
                if filename.endswith('.json'):
                    configs.append(filename[:-5])  # Remove .json extension
        return jsonify({"success": True, "configs": sorted(configs)})
    except Exception as e:
        logger.error(f"Config list error: {e}")
        return jsonify({"success": False, "error": str(e)})


@app.route('/api/config/delete/<config_name>', methods=['DELETE'])
def api_config_delete(config_name):
    """Delete a saved configuration"""
    try:
        config_path = os.path.join(config_dir, f"{config_name}.json")
        if os.path.exists(config_path):
            os.remove(config_path)
            return jsonify({"success": True, "message": f"Config '{config_name}' deleted"})
        return jsonify({"success": False, "error": "Config not found"})
    except Exception as e:
        logger.error(f"Config delete error: {e}")
        return jsonify({"success": False, "error": str(e)})


if __name__ == '__main__':
    # Run Flask app
    app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)
