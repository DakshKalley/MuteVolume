import speech_recognition as sr
import subprocess
r = sr.Recognizer()

mic = sr.Microphone()
with mic as source:
    print("Speak into the mic")
    r.adjust_for_ambient_noise(source)
    try:
        audio = r.listen(source)
        print(r.recognize_sphinx(audio))
        if (r.recognize_sphinx(audio)) == ('mute'):
            subprocess.call(['osascript', '-e', 'set volume 0'])
            print("volume muted")
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
