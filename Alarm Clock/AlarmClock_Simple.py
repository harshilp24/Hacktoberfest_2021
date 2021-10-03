
import datetime
from playsound import playsound

hours=int(input("Enter Hours : "))
min=int(input("Enter Minutes : "))
ampm=input("am / pm : ")


if ampm=="pm":
    hours+=12

while True:
    
     if(hours==datetime.datetime.now().hour and min==datetime.datetime.now().minute):
        print("playing")
        playsound("sound.wav")
        break