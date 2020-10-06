from tkinter import *
from math import *
expression=""
def input_number(number, equation):
   global expression
   if number=="<-":
      expression=expression[:len(expression)-1]
   else:
      expression = expression + str(number)
   equation.set(expression)

def clear_input_field(equation):
   global expression
   expression = ""
   equation.set("Enter the expression")
def evaluate(equation):
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = ""
    except:
        equation.set("check the entered equation")
        expression = ""
#create the tkinter screen and styling the screen
window=Tk()
window.configure(bg="lightgreen")
window.title("Calci")
window.geometry("300x300")
equation=StringVar()
input_field = Entry(window, textvariable=equation,bg="lightgreen",bd=0)
input_field.place(height=100)
input_field.grid(columnspan=5,ipadx=135,ipady=12)
equation.set("Enter the expression")
_1 = Button(window, text="1",fg="white",bg="black",bd=5,command=lambda: input_number(1,equation), height=2,width=5).place(x=0,y=50)
_2 = Button(window, text="2",fg="white",bg="black",bd=5,command=lambda: input_number(2,equation), height=2,width=5).place(x=60,y=50)
_3 = Button(window, text="3",fg="white",bg="black",bd=5,command=lambda: input_number(3,equation), height=2,width=5).place(x=120,y=50)
_4 = Button(window, text="4",fg="white",bg="black",bd=5,command=lambda: input_number(4,equation), height=2,width=5).place(x=0,y=100)
_5 = Button(window, text="5",fg="white",bg="black",bd=5,command=lambda: input_number(5,equation), height=2,width=5).place(x=60,y=100)
_6 = Button(window, text="6",fg="white",bg="black",bd=5,command=lambda: input_number(6,equation), height=2,width=5).place(x=120,y=100)
_7 = Button(window, text="7",fg="white",bg="black",bd=5,command=lambda: input_number(7,equation), height=2,width=5).place(x=0,y=150)
_8 = Button(window, text="8",fg="white",bg="black",bd=5,command=lambda: input_number(8,equation), height=2,width=5).place(x=60,y=150)
_9 = Button(window, text="9",fg="white",bg="black",bd=5,command=lambda: input_number(9,equation), height=2,width=5).place(x=120,y=150)
_0 = Button(window, text="0",fg="white",bg="black",bd=5,command=lambda: input_number(0,equation), height=2,width=5).place(x=0,y=200)
_00= Button(window, text="00",fg="white",bg="black",bd=5,command=lambda: input_number("00",equation), height=2,width=5).place(x=60,y=200)
bo= Button(window, text="(",fg="white",bg="black",bd=5,command=lambda: input_number("(",equation), height=2,width=5).place(x=60,y=250)
bc= Button(window, text=")",fg="white",bg="black",bd=5,command=lambda: input_number(")",equation), height=2,width=5).place(x=120,y=250)
sqrt1=Button(window, text="sqrt",fg="white",bg="black",bd=5,command=lambda: input_number("sqrt(",equation), height=2,width=5).place(x=240,y=50)
log101=Button(window, text="log10",fg="white",bg="black",bd=5,command=lambda: input_number("log10(",equation), height=2,width=5).place(x=240,y=100)
plus = Button(window, text='+', fg='white', bg='black', bd=5, command=lambda: input_number('+', equation), height=2, width=5).place(x=180,y=50)
minus = Button(window, text='-', fg='white', bg='black', bd=5, command=lambda: input_number('-', equation), height=2, width=5).place(x=180,y=100)
multiply = Button(window, text='*', fg='white', bg='black', bd=5, command=lambda:  input_number('*', equation), height=2, width=5).place(x=180,y=150)
divide = Button(window, text='/', fg='white', bg='black', bd=5, command=lambda: input_number('/', equation), height=2, width=5).place(x=180,y=200)
equal = Button(window, text='=', fg='white', bg='black', bd=5, command=lambda: evaluate(equation), height=2, width=5).place(x=120,y=200)
clear = Button(window, text='C', fg='white', bg='black', bd=5, command=lambda: clear_input_field(equation), height=2, width=5).place(x=0,y=250)
decimal=Button(window, text=".", fg="white", bg="black", bd=5, command=lambda: input_number(".",equation), height=2, width=5).place(x=180,y=250)
bac=Button(window, text="<-", fg="white", bg="black", bd=5, command=lambda: input_number("<-",equation), height=2, width=5).place(x=240,y=150)
