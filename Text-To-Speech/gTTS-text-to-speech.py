# Text-To-Speech Using gTTS API
# Use: pip install gTTS
# Use: pip install playsound
# Run this program in the command line:
# python gTTS-text-to-speech.py "<text>" --"<output filename>"

from gtts import gTTS
from playsound import playsound
from sys import argv, exit
import os

speechSettings = {
    "text": None,
    "output": "speech only",
    "language": 'en',
    "slow": False
    }

def main():
    if len(argv) < 2 or len(argv) > 3:
        print("Usage: python gTTS-text-to-speech.py \"<text>\" --\"<output filename>\"")
        exit()

def retrieveText():
    speechSettings["text"] = argv[1]

def retrieveOutputLocation():
    if len(argv) == 3:
        if argv[2][0] != "-" and argv[2][1] != "-":
            print("Usage: python gTTS-text-to-speech.py \"<text>\" --\"<output filename>\"")
            exit()
        saveFile = argv[2]
        speechSettings["output"] = saveFile.strip("--")
    
def output():
    speech = gTTS(text=speechSettings["text"], lang=speechSettings["language"], slow=speechSettings["slow"])

    if speechSettings["output"] == "speech only":
        speech.save("output.mp3")
        playsound("output.mp3")
        os.remove("output.mp3")

    else:
        try:
            speech.save(speechSettings["output"])
            playsound(speechSettings["output"])
        except:
            print("Output file path could not be found")
        
main()
retrieveText()
retrieveOutputLocation()
output()
