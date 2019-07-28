import speech_recognition as sr
r = sr.Recognizer()

mic = sr.Microphone()
with mic as source:
    print("Speak into the mic")
    r.adjust_for_ambient_noise(source)
    try:
        audio = r.listen(source)
        if (r.recognize_sphinx(audio)) == ('mute'):
            print("volume muted")
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
