#!/usr/bin/env python3
# 1. install gtts library using 'pip install gtts'
from gtts import gTTS

import os
# replace 'YOUR_TEXT_FILE' with name of your text file.
f=open('YOUR_TEXT_FILE')
x=f.read()

language='en'

audio=gTTS(text=x,lang=language,slow=False)

audio.save("1.wav")
os.system("1.wav")
# run this code in terminal
