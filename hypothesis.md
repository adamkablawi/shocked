We are to create a system that uses electromuscular stimulation alongside electroencephalography to deliver electrical pulses to a user, and measure brain response for neuro-feedback.

Components:
- EEG Headset
- EMS Device
- Laptop to coordinate stimulation and data

1. Establish a spectral power density baseline for the patient across different brain waves.

2. Start at a sub-threshold level, and increase the pulse intensity at increments of time.

3. Measure waves to find inidcators of pain and discomfort, create/find an indicator for stress/discomfort, stop when a threshold is met.


Notes:
- Alpha wave suppression is an indication of discomfort
- Beta elevation is an indicator of pain/stress
- Frontal Theta spikes are indiciations of pain processing
- We could probably make some kind of composite score from these to define an indiciator for overall discomfort
- Once this indicator meets a discomfort threshold, we stop the system or so?

Problem:
- EMS Artifacts in EEG response
    - We do temporal gating (measurement in a window after the stimulus)
    - Hardware blanking?
    - Placement as far as possible
    - Shorter PWs to decrease artifact duration


Diagram:

┌─────────────┐     trigger      ┌──────────────┐
│   Python    │ ───────────────► │   EMS Unit   │
│  Controller │                  └──────────────┘
│             │     LSL stream   ┌──────────────┐
│             │ ◄─────────────── │  EEG Headset │
└─────────────┘                  └──────────────┘
       │
       ▼
  Epoch → Clean → Extract features → Compare to baseline → Decision