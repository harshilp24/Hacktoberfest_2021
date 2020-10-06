#You can use this module for offline TTS (Text to speech)
'''
Use:
pip install pyttsx3
'''
import pyttsx3

#set this variable to what you want to say
to_say = "Hey Hacktoberfest"

speaking_engine = pyttsx3.init()
speaking_engine.say(to_say)

#will hold the program till the phrase is completely spoken
speaking_engine.runAndWait()

'''
Some Extra Features :


to set the volume:
speaking_engine.setProperty('volume',1.0)


to set the speaking rate:
speaking_engine.setProperty('rate', 125)

to save as MP3:
speaking_engine.save_to_file('Hello World', 'test.mp3')
'''
