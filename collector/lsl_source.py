import pylsl

def connect(stream_type='EEG', timeout=10):
    """Resolve an LSL stream and return (inlet, srate, n_ch, channel_names)."""
    print(f"Connecting to {stream_type} stream...")
    streams = pylsl.resolve_byprop('type', stream_type, timeout=timeout)
    if not streams:
        raise RuntimeError(f"No {stream_type} stream found.")

    inlet = pylsl.StreamInlet(streams[0])
    info = inlet.info()
    srate = float(info.nominal_srate())
    n_ch = info.channel_count()

    channel_names = []
    ch = info.desc().child('channels').child('channel')
    for i in range(n_ch):
        label = ch.child_value('label')
        channel_names.append(label if label else f'Ch{i + 1}')
        ch = ch.next_sibling()

    return inlet, srate, n_ch, channel_names
