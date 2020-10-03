import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()

def recognize_sound():
    with mic as source:
        audio = r.listen(source)
    
    try:
        recog = r.recognize_google(audio)
        return recog
    except:
        return "Error"


while True:
    a = input("Recognize Sound? y/n  ")
    if a == "y":
        print(f"\n\n{recognize_sound()}")
    else:
        exit()
