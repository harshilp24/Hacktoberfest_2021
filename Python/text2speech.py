from gtts import gTTS
from playsound import playsound
import os

Input = input("Enter what you want to be converted to speech >> ")

tts = gTTS(Input, lang='en', slow=False)

tts.save("text2speech.mp3") 
playsound('text2speech.mp3')
os.remove("text2speech.mp3")
