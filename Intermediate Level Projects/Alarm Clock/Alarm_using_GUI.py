import time
import datetime
from playsound import playsound

window=Tk()



window.title("Alarm Clock")
window.geometry('500x200')
hour=0
minutes=0
ampm="am"

def setTime():
    hour=hours.get()
    minutes=mins.get()
    ampm=ampms.get()
    if ampm=="pm":
      hour+=12
    while True:
    
      if(hour==datetime.datetime.now().hour and minutes==datetime.datetime.now().minute):
        print("playing")
        print(hour,minutes,ampm)
        playsound("sound.wav")
       
        #time.sleep(8000)
        
        break


    
    
label1=Label(window,text="Hours : ",fg='black',font=('Arial',14))
label1.grid(row=0,column=0,padx=3)

hours=IntVar()

textbox1=Entry(window,textvariable=hours,fg='black',font=('Arial,14'))
textbox1.grid(row=0,column=1)


label2=Label(window,text="Min : ",fg='black',font=('Arial',14))
label2.grid(row=1,column=0,padx=5)

mins=IntVar()

textbox2=Entry(window,textvariable=mins,fg='black',font=('Arial,14'))
textbox2.grid(row=1,column=1)

label3=Label(window,text="AM/PM : ",fg='black',font=('Arial',14))
label3.grid(row=2,column=0,padx=5)

ampms=StringVar()

textbox3=Entry(window,textvariable=ampms,fg='black',font=('Arial,14'))
textbox3.grid(row=2,column=1)



button=Button(window,command=setTime,text='Save',fg='black',font=('Arial',14))
button.grid(row=4,column=1)

window.mainloop()
