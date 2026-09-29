// ============ EMS Controller Web App ============

// State
let state = {
    connected: false,
    mode: 'ems',
    intensity: 0.15,
    sineFreq: 40,
    emsFreq: 35,
    gap: 100,
    pulseWidth: 20,
    offset: 0.50,
    burstDuration: 1.0,
    alternatingBurst: false
};

const ALTERNATING_BURST_ON_SECONDS = 0.5;
const ALTERNATING_BURST_ON_MS = 500;
const ALTERNATING_BURST_OFF_MS = 500;
let alternatingBurstActive = false;
let alternatingBurstTimer = null;

// DOM Elements
const connectBtn = document.getElementById('connectBtn');
const disconnectBtn = document.getElementById('disconnectBtn');
const statusIndicator = document.getElementById('statusIndicator');
const statusMessage = document.getElementById('statusMessage');
const statusDot = statusIndicator.querySelector('.status-dot');
const statusText = statusIndicator.querySelector('.status-text');

const modeRadios = document.querySelectorAll('input[name="mode"]');
const intensitySlider = document.getElementById('intensitySlider');
const intensityValue = document.getElementById('intensityValue');
const sineFreqSlider = document.getElementById('sineFreqSlider');
const sineFreqValue = document.getElementById('sineFreqValue');
const emsFreqSlider = document.getElementById('emsFreqSlider');
const emsFreqValue = document.getElementById('emsFreqValue');
const gapSlider = document.getElementById('gapSlider');
const gapValue = document.getElementById('gapValue');
const pulseWidthSlider = document.getElementById('pulseWidthSlider');
const pulseWidthValue = document.getElementById('pulseWidthValue');
const offsetInput = document.getElementById('offsetInput');
const burstDurationSlider = document.getElementById('burstDurationSlider');
const burstDurationInput = document.getElementById('burstDurationInput');
const burstDurationValue = document.getElementById('burstDurationValue');
const alternatingBurstCheckbox = document.getElementById('alternatingBurstCheckbox');
const sendBurstBtn = document.getElementById('sendBurstBtn');
const rawCommandInput = document.getElementById('rawCommandInput');
const logArea = document.getElementById('logArea');
const configName = document.getElementById('configName');
const configSelect = document.getElementById('configSelect');
const configPreview = document.getElementById('configPreview');

// ============ Tab Navigation ============
document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
        const tab = e.target.dataset.tab;
        
        // Hide all tabs
        document.querySelectorAll('.tab-content').forEach(tc => {
            tc.classList.remove('active');
        });
        
        // Remove active from all buttons
        document.querySelectorAll('.tab-btn').forEach(b => {
            b.classList.remove('active');
        });
        
        // Show selected tab
        document.getElementById(tab).classList.add('active');
        e.target.classList.add('active');
        
        // Reload config list if config tab
        if (tab === 'config') {
            loadConfigList();
        }
    });
});

// ============ Event Listeners ============
connectBtn.addEventListener('click', connect);
disconnectBtn.addEventListener('click', disconnect);

modeRadios.forEach(radio => {
    radio.addEventListener('change', (e) => {
        state.mode = e.target.value;
        addLog(`Mode changed to: ${state.mode.toUpperCase()}`, 'sent');
    });
});

intensitySlider.addEventListener('input', (e) => {
    state.intensity = parseFloat(e.target.value);
    intensityValue.textContent = state.intensity.toFixed(2);
});

sineFreqSlider.addEventListener('input', (e) => {
    state.sineFreq = parseInt(e.target.value);
    sineFreqValue.textContent = state.sineFreq;
});

emsFreqSlider.addEventListener('input', (e) => {
    state.emsFreq = parseInt(e.target.value);
    emsFreqValue.textContent = state.emsFreq;
});

gapSlider.addEventListener('input', (e) => {
    state.gap = parseInt(e.target.value);
    gapValue.textContent = state.gap;
});

pulseWidthSlider.addEventListener('input', (e) => {
    state.pulseWidth = parseInt(e.target.value);
    pulseWidthValue.textContent = state.pulseWidth;
});

burstDurationSlider.addEventListener('input', (e) => {
    state.burstDuration = parseFloat(e.target.value);
    burstDurationValue.textContent = state.burstDuration.toFixed(1);
    burstDurationInput.value = '';  // Clear manual input when slider changes
});

burstDurationInput.addEventListener('input', (e) => {
    const val = parseFloat(e.target.value);
    if (!isNaN(val) && val >= 0.1 && val <= 60.0) {
        state.burstDuration = val;
        burstDurationValue.textContent = val.toFixed(1);
        burstDurationSlider.value = val;
    }
});

alternatingBurstCheckbox.addEventListener('change', (e) => {
    state.alternatingBurst = e.target.checked;
    updateBurstControlUI();

    if (!state.alternatingBurst && alternatingBurstActive) {
        stopAlternatingBurst(true);
    }
});

offsetInput.addEventListener('input', (e) => {
    const val = parseFloat(e.target.value);
    if (!isNaN(val)) {
        state.offset = Math.max(0, Math.min(1, val));
    }
});

// ============ Connection ============
async function connect() {
    connectBtn.disabled = true;
    disconnectBtn.disabled = true;
    showStatus('Scanning for device...', 'info');
    addLog('Connecting...', 'sent');
    
    try {
        const response = await fetch('/api/scan', { method: 'POST' });
        let data = {};
        const responseText = await response.text();
        try {
            data = responseText ? JSON.parse(responseText) : {};
        } catch (parseError) {
            data = {
                success: false,
                error: `Backend returned non-JSON response: ${responseText || response.statusText}`
            };
        }
        
        if (response.ok && data.success) {
            state.connected = true;
            updateConnectionUI();
            showStatus('Connected to EMS Controller', 'success');
            addLog('Connected to EMS Controller', 'received');
        } else {
            const errorMessage = data.error || `HTTP ${response.status}: ${response.statusText || 'scan request failed'}`;
            showStatus('Failed to connect: ' + errorMessage, 'error');
            addLog('Connection failed: ' + errorMessage, 'error');
            console.error('Connection failed', { status: response.status, data, responseText });
        }
    } catch (error) {
        showStatus('Error: ' + error.message, 'error');
        addLog('Connection error: ' + error.message, 'error');
    }
    
    updateConnectionUI();
}

async function disconnect() {
    disconnectBtn.disabled = true;
    connectBtn.disabled = true;
    stopAlternatingBurst(false);
    
    try {
        const response = await fetch('/api/disconnect', { method: 'POST' });
        const data = await response.json();
        if (!response.ok || data.success === false) {
            addLog('Disconnect warning: ' + (data.error || 'backend did not confirm disconnect'), 'error');
        }
        state.connected = false;
        updateConnectionUI();
        addLog('Disconnected', 'sent');
        showStatus('Disconnected', 'info');
    } catch (error) {
        addLog('Disconnect error: ' + error.message, 'error');
        state.connected = false;
        updateConnectionUI();
        showStatus('Disconnected locally; backend did not respond', 'error');
    }
}

function updateConnectionUI() {
    if (state.connected) {
        connectBtn.disabled = true;
        disconnectBtn.disabled = false;
        statusDot.classList.add('connected');
        statusText.textContent = 'Connected';
    } else {
        connectBtn.disabled = false;
        disconnectBtn.disabled = true;
        statusDot.classList.remove('connected');
        statusText.textContent = 'Disconnected';
    }
}

// ============ Commands ============
async function sendCommand(command) {
    if (!state.connected) {
        showStatus('Not connected to device', 'error');
        return false;
    }
    
    try {
        const response = await fetch('/api/send', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ command })
        });
        const data = await response.json();
        
        if (data.success) {
            addLog(`> ${command}`, 'sent');
            return true;
        } else {
            addLog(`Error: ${data.error || 'Send failed'}`, 'error');
            return false;
        }
    } catch (error) {
        addLog(`Error: ${error.message}`, 'error');
        return false;
    }
}

async function sendAllSettings() {
    if (!state.connected) {
        showStatus('Not connected to device', 'error');
        return;
    }
    
    const commands = [
        `mode=${state.mode}`,
        `amp=${state.intensity.toFixed(2)}`,
        `fs=${state.sineFreq}`,
        `fe=${state.emsFreq}`,
        `gap=${state.gap}`,
        `pw=${state.pulseWidth}`,
        `offset=${state.offset.toFixed(2)}`,
        `bd=${state.burstDuration.toFixed(2)}`
    ];
    
    for (const cmd of commands) {
        await sendCommand(cmd);
        await new Promise(resolve => setTimeout(resolve, 100));
    }
    
    showStatus('All settings sent', 'success');
}

async function sendBurst() {
    if (state.alternatingBurst) {
        if (alternatingBurstActive) {
            stopAlternatingBurst(true);
        } else {
            await startAlternatingBurst();
        }
        return;
    }

    const duration = burstDurationInput.value.trim();
    const burstCmd = duration ? `b=${parseFloat(duration).toFixed(2)}` : `b=${state.burstDuration.toFixed(2)}`;
    await sendCommand(burstCmd);
}

async function sendStop() {
    stopAlternatingBurst(false);
    await sendCommand('stop');
}

function scheduleAlternatingBurstStep(delayMs, step) {
    clearAlternatingBurstTimer();
    alternatingBurstTimer = setTimeout(step, delayMs);
}

function clearAlternatingBurstTimer() {
    if (alternatingBurstTimer) {
        clearTimeout(alternatingBurstTimer);
        alternatingBurstTimer = null;
    }
}

async function startAlternatingBurst() {
    if (!state.connected) {
        showStatus('Not connected to device', 'error');
        return;
    }

    alternatingBurstActive = true;
    updateBurstControlUI();
    showStatus('Alternating burst started: 0.5 sec ON / 0.5 sec OFF', 'success');
    addLog('Alternating burst started: 0.5s ON / 0.5s OFF', 'sent');
    await runAlternatingBurstOnPhase();
}

async function runAlternatingBurstOnPhase() {
    if (!alternatingBurstActive) return;

    const ok = await sendCommand(`b=${ALTERNATING_BURST_ON_SECONDS.toFixed(2)}`);
    if (!ok) {
        stopAlternatingBurst(false);
        showStatus('Alternating burst stopped: failed to send burst', 'error');
        return;
    }

    scheduleAlternatingBurstStep(ALTERNATING_BURST_ON_MS, runAlternatingBurstOffPhase);
}

async function runAlternatingBurstOffPhase() {
    if (!alternatingBurstActive) return;

    const ok = await sendCommand('stop');
    if (!ok) {
        stopAlternatingBurst(false);
        showStatus('Alternating burst stopped: failed to send stop', 'error');
        return;
    }

    scheduleAlternatingBurstStep(ALTERNATING_BURST_OFF_MS, runAlternatingBurstOnPhase);
}

function stopAlternatingBurst(sendStopCommand) {
    if (!alternatingBurstActive) {
        clearAlternatingBurstTimer();
        updateBurstControlUI();
        return;
    }

    alternatingBurstActive = false;
    clearAlternatingBurstTimer();
    updateBurstControlUI();
    addLog('Alternating burst stopped', 'sent');

    if (sendStopCommand && state.connected) {
        sendCommand('stop');
    }
}

function updateBurstControlUI() {
    if (!sendBurstBtn || !alternatingBurstCheckbox) return;

    if (state.alternatingBurst) {
        sendBurstBtn.textContent = alternatingBurstActive ? 'Stop Alternating Burst' : 'Start Alternating Burst';
    } else {
        sendBurstBtn.textContent = 'Send Burst';
    }
}

async function sendRawCommand() {
    const cmd = rawCommandInput.value.trim();
    if (!cmd) return;
    
    await sendCommand(cmd);
    rawCommandInput.value = '';
}

// ============ Configuration ============
async function saveConfiguration() {
    const name = configName.value.trim();
    if (!name) {
        showStatus('Please enter a configuration name', 'error');
        return;
    }
    
    const config = {
        mode: state.mode,
        intensity: state.intensity,
        sineFreq: state.sineFreq,
        emsFreq: state.emsFreq,
        gap: state.gap,
        pulseWidth: state.pulseWidth,
        offset: state.offset,
        burstDuration: state.burstDuration,
        alternatingBurst: state.alternatingBurst
    };
    
    try {
        const response = await fetch('/api/config/save', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, config })
        });
        const data = await response.json();
        
        if (data.success) {
            showStatus(`Configuration saved: ${name}`, 'success');
            configName.value = '';
            loadConfigList();
            addLog(`Configuration saved: ${name}`, 'received');
        } else {
            showStatus('Save failed: ' + (data.error || 'Unknown error'), 'error');
        }
    } catch (error) {
        showStatus('Error: ' + error.message, 'error');
    }
}

async function loadConfigList() {
    try {
        const response = await fetch('/api/config/list');
        const data = await response.json();
        
        if (data.success) {
            configSelect.innerHTML = '';
            data.configs.forEach(config => {
                const option = document.createElement('option');
                option.value = config;
                option.textContent = config;
                configSelect.appendChild(option);
            });
        }
    } catch (error) {
        console.error('Error loading config list:', error);
    }
}

async function loadConfiguration() {
    const name = configSelect.value;
    if (!name) return;
    
    try {
        const response = await fetch(`/api/config/load/${name}`);
        const data = await response.json();
        
        if (data.success) {
            const config = data.config;
            state.mode = config.mode || 'ems';
            state.intensity = config.intensity || 0.15;
            state.sineFreq = config.sineFreq || 40;
            state.emsFreq = config.emsFreq || 35;
            state.gap = config.gap || 100;
            state.pulseWidth = config.pulseWidth || 20;
            state.offset = config.offset || 0.50;
            state.burstDuration = config.burstDuration || 1.0;
            state.alternatingBurst = Boolean(config.alternatingBurst);
            
            updateUIFromState();
            updateConfigPreview();
            showStatus(`Configuration loaded: ${name}`, 'success');
            addLog(`Configuration loaded: ${name}`, 'received');
        } else {
            showStatus('Load failed: ' + (data.error || 'Unknown error'), 'error');
        }
    } catch (error) {
        showStatus('Error: ' + error.message, 'error');
    }
}

async function deleteConfiguration() {
    const name = configSelect.value;
    if (!name) return;
    
    if (!confirm(`Delete configuration "${name}"?`)) return;
    
    try {
        const response = await fetch(`/api/config/delete/${name}`, { method: 'DELETE' });
        const data = await response.json();
        
        if (data.success) {
            showStatus(`Configuration deleted: ${name}`, 'success');
            loadConfigList();
            addLog(`Configuration deleted: ${name}`, 'sent');
        } else {
            showStatus('Delete failed: ' + (data.error || 'Unknown error'), 'error');
        }
    } catch (error) {
        showStatus('Error: ' + error.message, 'error');
    }
}

function updateUIFromState() {
    document.querySelector(`input[name="mode"][value="${state.mode}"]`).checked = true;
    intensitySlider.value = state.intensity;
    intensityValue.textContent = state.intensity.toFixed(2);
    sineFreqSlider.value = state.sineFreq;
    sineFreqValue.textContent = state.sineFreq;
    emsFreqSlider.value = state.emsFreq;
    emsFreqValue.textContent = state.emsFreq;
    gapSlider.value = state.gap;
    gapValue.textContent = state.gap;
    pulseWidthSlider.value = state.pulseWidth;
    pulseWidthValue.textContent = state.pulseWidth;
    offsetInput.value = state.offset.toFixed(2);
    burstDurationSlider.value = state.burstDuration;
    burstDurationValue.textContent = state.burstDuration.toFixed(1);
    alternatingBurstCheckbox.checked = state.alternatingBurst;
    updateBurstControlUI();
}

function updateConfigPreview() {
    const config = {
        mode: state.mode,
        intensity: state.intensity,
        sineFreq: state.sineFreq,
        emsFreq: state.emsFreq,
        gap: state.gap,
        pulseWidth: state.pulseWidth,
        offset: state.offset,
        burstDuration: state.burstDuration,
        alternatingBurst: state.alternatingBurst
    };
    configPreview.textContent = JSON.stringify(config, null, 2);
}

// ============ Utility Functions ============
function showStatus(message, type) {
    statusMessage.textContent = message;
    statusMessage.className = `status-message ${type}`;
}

function addLog(line, type = 'info') {
    const logLine = document.createElement('div');
    logLine.className = `log-line ${type}`;
    const time = new Date().toLocaleTimeString('en-US', { hour12: false, hour: '2-digit', minute: '2-digit', second: '2-digit' });
    logLine.textContent = `[${time}] ${line}`;
    logArea.appendChild(logLine);
    logArea.scrollTop = logArea.scrollHeight;
}

function clearLog() {
    logArea.innerHTML = '';
}

// ============ Initialization ============
document.addEventListener('DOMContentLoaded', () => {
    updateConnectionUI();
    updateBurstControlUI();
    loadConfigList();
    updateConfigPreview();
    addLog('Application started', 'info');
    
    // Check connection status periodically
    setInterval(async () => {
        try {
            const response = await fetch('/api/status');
            const data = await response.json();
            if (data.connected !== state.connected) {
                state.connected = data.connected;
                if (!state.connected) {
                    stopAlternatingBurst(false);
                }
                updateConnectionUI();
                addLog(state.connected ? 'Device connected' : 'Device disconnected', 'received');
            }
        } catch (error) {
            // Connection check failed, likely backend is down
        }
    }, 2000);
});
