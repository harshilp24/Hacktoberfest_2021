# importing whole module
from tkinter import Label, Tk 
#importing time
import time

# creating tkinter window
app_window = Tk() 
app_window.title("Digital Clock") 
app_window.geometry("420x150") 
app_window.resizable(3,3)

# Styling the label widget so that clock
# will look more attractive
text_font= ("Boulder", 68, 'bold')
background = "#393E46"
foreground= "#3E00FF"
border_width = 25

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width) 
label.grid(row=0, column=1)

def digital_clock(): 
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live) 
   label.after(200, digital_clock)

digital_clock()
app_window.mainloop()