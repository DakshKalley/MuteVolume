import speech_recognition as sr
import subprocess
r = sr.Recognizer()
mic = sr.Microphone()

while True:
    with mic as source:
        print("Speak into the mic")
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source)
            print(r.recognize_google(audio))
            if (r.recognize_google(audio)) == ('mute'):
                subprocess.call(['osascript', '-e', 'set volume with output muted'])
                print("volume muted")
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Voice error; {0}".format(e))
