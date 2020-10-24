
from tkinter import *
from timeit import default_timer as timer
from PIL import ImageTk,Image
import random

window = Tk()
#Dimensions for the gui window
window.geometry("500x200")
window.title('Speed typing test')
window.configure(background="Sky blue")

#here the path of the image should uploaded to set it in the window
my_img= ImageTk.PhotoImage(Image.open("...."))

my_label=Label(image=my_img)
my_label.pack()
x=0

def game():
    global x


    if x == 0:
        window.destroy()
        x = x + 1


    def check_result():
        if entry.get() == words[word]:

            end = timer()


            print(end - start)
        else:
            print("Wrong Input")

    words = ['Data Structure', 'Machine Learning', 'Algorithm',
             'Hackathon', 'Hactoberfest', 'Software']

    # Give random words for testing the speed of user
    word = random.randint(0, (len(words) - 1))

    # start timer using timeit function
    start = timer()
    windows = Tk()
    windows.geometry("450x250")


    label2= Label(windows, text=words[word], font="times 20")


    label2.place(x=150, y=10)
    label3 = Label(windows, text="Start Typing", font="times 20")
    label3.place(x=10, y=50)

    entry = Entry(windows)
    entry.place(x=280, y=55)

#button created to opearte the program
    btn2 = Button(windows, text="Done",
                command=check_result, width=12, bg='grey')
    btn2.place(x=150, y=100)

    btn3 = Button(windows, text="Try Again",
                command=game, width=12, bg='grey')
    btn3.place(x=250, y=100)
    windows.mainloop()


label1 = Label(window, text="Lets start playing..", font="times 20")
label1.place(x=10, y=50)

btn1 = Button(window, text="Go", command=game, width=12, bg='grey')
btn1.place(x=150, y=100)

# calling window
window.mainloop()



