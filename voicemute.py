from vosk import Model, KaldiRecognizer
import pyaudio
import objc


model = Model(r"vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()


def mute_volume():
    script = '''
    tell application "System Events"
        set volume with output muted
    end tell
    '''
    
    NSAppleScript = objc.lookUpClass('NSAppleScript')
    apple_script = NSAppleScript.alloc().initWithSource_(script)
    apple_script.executeAndReturnError_(None)

def unmute_volume():
    script = '''
    tell application "System Events"
        set volume without output muted
    end tell
    '''
    
    NSAppleScript = objc.lookUpClass('NSAppleScript')
    apple_script = NSAppleScript.alloc().initWithSource_(script)
    apple_script.executeAndReturnError_(None)


while True:
        data = stream.read(4096, exception_on_overflow = False)
        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()
            cmd = (text[14:-3])
            print(cmd)
            if (cmd == 'mute'):
                mute_volume()
                print("volume muted")
            if (cmd == 'speak'):
                unmute_volume()
                print("volume unmuted")
