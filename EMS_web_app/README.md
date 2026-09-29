# EMS Controller Web App

A cross-platform web application for controlling the EMS (Electrical Muscle Stimulation) device via Bluetooth Low Energy (BLE). This app provides the same functionality as the Android app plus configuration save/load capabilities.

## Features

✅ **Real-time BLE Communication** - Connect and control EMS device wirelessly  
✅ **Waveform Modes** - Switch between EMS and Sine wave modes  
✅ **Full Parameter Control** - Adjust intensity, frequency, gap, pulse width, offset, and burst duration  
✅ **Configuration Management** - Save and load configurations as JSON files  
✅ **Cross-Platform** - Works on Windows, macOS, and Linux  
✅ **Self-Contained** - No installation needed, everything bundled together  
✅ **Beautiful UI** - Modern, responsive interface with real-time updates  

## System Requirements

- **Python 3.10+** (or just use the bundled executable)
- **Bluetooth 5.0+** hardware support
- Any modern web browser (Chrome, Firefox, Safari, Edge)

## Quick Start

### Option 1: Run from Source (Linux/macOS)

```bash
cd EMS_web_app
chmod +x run.sh
./run.sh
```

The app will:
1. Check for Python
2. Install dependencies automatically
3. Start the Flask server
4. Open your browser to http://localhost:5000

### Option 2: Run from Source (Windows)

Double-click `run.bat` and it will:
1. Check for Python
2. Install dependencies automatically  
3. Start the Flask server
4. Open your browser

### Option 3: Portable Executable (All Platforms)

[Coming Soon] PyInstaller bundled executables will be provided in releases.

## Usage

1. **Connect to Device**
   - Click "Connect to Device" button
   - App will scan for "EMS Controller" device
   - Once connected, status indicator will turn green

2. **Control Parameters**
   - **Waveform Mode**: Select between EMS and Sine wave
   - **Intensity**: Adjust output amplitude (0.0 - 0.25)
   - **Sine Frequency**: Set frequency when in Sine mode (1 - 200 Hz)
   - **EMS Frequency**: Set frequency for EMS pulses (10 - 200 Hz, min 10 Hz)
   - **Gap**: Pulse spacing in microseconds (0 - 2000 μs)
   - **Pulse Width**: Duty cycle percentage (1 - 100%)
   - **Offset**: DC bias level (0.0 - 1.0)
   - **Burst Duration**: How long each burst lasts (0.1 - 60 seconds)

3. **Send Commands**
   - **Send All Settings**: Applies all current settings to device
   - **Send Burst**: Triggers a single burst with current duration
   - **Alternate 0.5 sec ON / 0.5 sec OFF**: When checked, the burst button starts/stops repeated `b=0.50`, `stop` cycling
   - **Stop**: Stops any active stimulation
   - **Raw Command**: For advanced users - send custom commands

4. **Save Configurations**
   - Adjust all parameters to your desired values
   - Go to "Configuration" tab
   - Enter a name and click "Save Current Config"
   - Configurations are saved to the app-local `configurations/` folder

5. **Load Configurations**
   - Go to "Configuration" tab
   - Select configuration from dropdown
   - Click "Load Config" to apply all parameters
   - Delete old configs as needed

## Supported BLE Commands

The app sends the same commands as the Android version:

| Command | Format | Example |
|---------|--------|---------|
| Mode | `mode=ems\|sine` | `mode=ems` |
| Amplitude | `amp=<float>` | `amp=0.15` |
| Sine Frequency | `fs=<int>` | `fs=40` |
| EMS Frequency | `fe=<int>` | `fe=35` |
| Gap | `gap=<int>` | `gap=100` |
| Pulse Width | `pw=<int>` | `pw=20` |
| Offset | `offset=<float>` | `offset=0.50` |
| Burst Duration | `bd=<float>` | `bd=1.5` |
| Burst | `b=<float>` | `b=2.0` |
| Stop | `stop` | `stop` |
| Info | `info` | `info` |

## Configuration Files

Configurations are automatically saved as JSON in:
- `configurations/` inside the `EMS_web_app` folder

Example configuration file (`example.json`):
```json
{
  "mode": "ems",
  "intensity": 0.15,
  "sineFreq": 40,
  "emsFreq": 35,
  "gap": 100,
  "pulseWidth": 20,
  "offset": 0.5,
  "burstDuration": 1.0
}
```

## Troubleshooting

### "Python is not installed"
Install Python 3.10+ from https://www.python.org/downloads/

### "Bluetooth is disabled"
Enable Bluetooth in your system settings

### "Device not found"
- Check if ESP32 is powered on and advertising
- Verify device name is "EMS Controller"
- Try moving closer to the device
- Restart the app and try again

### App won't start
- Check if port 5000 is available (not used by another app)
- Try restarting your computer
- Check console output for specific error messages

### Can't install dependencies
Run manually:
```bash
python -m pip install -r requirements.txt
```

On Windows with Python 3.13, if `bleak-winrt` appears in the error log, the app
is using an old dependency set. Update `requirements.txt` and run `run.bat`
again.

## File Structure

```
EMS_web_app/
├── app.py                 # Flask backend with BLE communication
├── requirements.txt       # Python dependencies
├── run.sh                 # Linux/macOS launcher script
├── run.bat                # Windows launcher script
├── README.md              # This file
├── templates/
│   └── index.html         # Main HTML interface
└── static/
    ├── css/
    │   └── style.css      # Styling (modern purple theme)
    └── js/
        └── app.js         # Frontend logic and UI controls
```

## Building Portable Executables

To create standalone executables for distribution:

### Windows
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --add-data "templates:templates" --add-data "static:static" app.py
```

### macOS/Linux
```bash
pip install pyinstaller
pyinstaller --onefile --add-data "templates:templates" --add-data "static:static" app.py
```

## Technical Details

- **Backend**: Flask 2.3+, Bleak (cross-platform BLE)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Protocol**: Nordic UART Service (NUS) BLE profile
- **Communication**: HTTP/JSON API with async BLE handling

## License

Same as EMS Controller project

## Support

For issues or feature requests, please refer to the main EMS Controller project repository.
