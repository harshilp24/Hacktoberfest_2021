# Text-To-Speech Using gTTS API
# Use: pip install gTTS
# Run this program in the command line:
# python gTTS-text-to-speech.py "<text>" "<output filename>" --language --slow

from gtts import gTTS
from sys import argv, exit
import os

speech = {
    "text": None,
    "output": None,
    "language": 'en',
    "slow": False
    }
#language = 'en'

#speech = gTTS(text=textInput, lang=language, slow=True)

#speech.save("welcome.mp3")

#print("Playing audio")
#os.system("mpg321 welcome.mp3")

def main():
    if len(argv) < 3 or len(argv) > 4:
        print("Usage: python gTTS-text-to-speech.py \"<text>\" \"<output filename>\" --language --slow")
        exit()
    
def retrieveText():
    speech["text"] = argv[1]
    print("speech[\"text\"] = " + speech["text"])

def saveOutput():
    speech["output"] = argv[2]
    print("speech[\"output\"] = " + speech["output"])

def configuration():
    print("test")
    
main()
retrieveText()

