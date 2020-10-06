from tkinter import *
import tkinter.messagebox

root = Tk()
root.geometry("1000x750+0+0")
root.title("Tic Tac Toe")
root.configure(background = 'blue')
Tops = Frame(root,bg = 'blue',pady = 2, width =1350, height = 100, relief = RIDGE)
Tops.grid(row=0,column=0)
flag =0

lblTitle = Label(Tops,font=('arial',50,'bold'),text = "Tic Tac Toe",bd = 21,fg='white', bg='blue',justify = CENTER)
lblTitle.grid(row=0,column=0)

MainFrame = Frame(root,bg = '#ffb84d',pady = 2, width =1350, height = 100, relief = RIDGE)
MainFrame.grid(row=1,column=0)

LeftFrame = Frame(MainFrame ,bd=10, width =750, height=500, pady=2,padx=10,bg='#ffb84d'  ,relief=RIDGE)
LeftFrame.pack(side=LEFT)

RightFrame  =  Frame(MainFrame ,bd=10, width =750, height=500, padx=10,pady=2,bg='#ffb84d',relief=RIDGE)
RightFrame.pack(side=RIGHT)

RightFrame1 = Frame(RightFrame ,bd=10, width =600, height=200, padx=10,pady=2, bg='#ffb84d', relief=RIDGE)
RightFrame1.grid(row=0,column=0)

RightFrame2  =  Frame(RightFrame ,bd=10, width =560, height=360, padx=10,pady=2, bg='#ffb84d',relief=RIDGE)
RightFrame2.grid(row=1,column=0)

PlayerX=IntVar()
PlayerO=IntVar()

PlayerX.set(0)
PlayerO.set(0)
Player1 = StringVar()
Player2 = StringVar()
pa = StringVar()
pb = StringVar()

buttons = StringVar()
click = True
def checker(buttons):
    global click
    if buttons["text"] == " " and click == True:        
        buttons["text"] = "X"
        buttons.configure(background = "white",fg = 'blue')
        click = False
        scorekeeper()
    elif buttons["text"] == " " and click == False:        
        buttons["text"] = "O"
        buttons.configure(background = "white",fg = 'red')
        click = True
        scorekeeper()

def scorekeeper():
		global pa,pb,Player1,Player2
		if (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X"):
			button1.configure(background = '#90ff0a')
			button2.configure(background = '#90ff0a')
			button3.configure(background = '#90ff0a')
			n = int(PlayerX.get())
			score = (n+1)
			PlayerX.set(score)
			pa = Player1.get() + " Won the Game!!"
			tkinter.messagebox.showinfo("Tic Tac Toe",pa)
			reset()
		if (button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X"):
			button4.configure(background = '#90ff0a')
			button5.configure(background = '#90ff0a')
			button6.configure(background = '#90ff0a')
			n = int(PlayerX.get())
			score = (n+1)
			PlayerX.set(score)
			pa = Player1.get() + " Won the Game!!"
			tkinter.messagebox.showinfo("Tic Tac Toe",pa)
			reset()
		if (button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X"):
			button7.configure(background = '#90ff0a')
			button8.configure(background = '#90ff0a')
			button9.configure(background = '#90ff0a')
			n = int(PlayerX.get())
			score = (n+1)
			PlayerX.set(score)
			pa = Player1.get() + " Won the Game!!"
			tkinter.messagebox.showinfo("Tic Tac Toe",pa)
			reset()
		if (button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X"):
			button1.configure(background = '#90ff0a')
			button4.configure(background = '#90ff0a')
			button7.configure(background = '#90ff0a')
			n = int(PlayerX.get())
			score = (n+1)
			PlayerX.set(score)
			pa = Player1.get() + " Won the Game!!"
			tkinter.messagebox.showinfo("Tic Tac Toe",pa)
			reset()
		if (button5["text"] == "X" and button2["text"] == "X" and button8["text"] == "X"):
			button5.configure(background = '#90ff0a')
			button2.configure(background = '#90ff0a')
			button8.configure(background = '#90ff0a')
			n = int(PlayerX.get())
			score = (n+1)
			PlayerX.set(score)
			pa = Player1.get() + " Won the Game!!"
			tkinter.messagebox.showinfo("Tic Tac Toe",pa)
			reset()
		if (button6["text"] == "X" and button9["text"] == "X" and button3["text"] == "X"):
			button6.configure(background = '#90ff0a')
			button9.configure(background = '#90ff0a')
			button3.configure(background = '#90ff0a')
			n = int(PlayerX.get())
			score = (n+1)
			PlayerX.set(score)
			pa = Player1.get() + " Won the Game!!"
			tkinter.messagebox.showinfo("Tic Tac Toe",pa)
			reset()
		if (button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X"):
			button1.configure(background = '#90ff0a')
			button5.configure(background = '#90ff0a')
			button9.configure(background = '#90ff0a')
			n = int(PlayerX.get())
			score = (n+1)
			PlayerX.set(score)
			pa = Player1.get() + " Won the Game!!"
			tkinter.messagebox.showinfo("Tic Tac Toe",pa)
			reset()
		if (button5["text"] == "X" and button7["text"] == "X" and button3["text"] == "X"):
			button5.configure(background = '#90ff0a')
			button7.configure(background = '#90ff0a')
			button3.configure(background = '#90ff0a')
			n = int(PlayerX.get())
			score = (n+1)
			PlayerX.set(score)
			pa = Player1.get() + " Won the Game!!"
			tkinter.messagebox.showinfo("Tic Tac Toe",pa)
			reset()
		# for O
		if (button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O"):
			button1.configure(background = '#90ff0a')
			button2.configure(background = '#90ff0a')
			button3.configure(background = '#90ff0a')
			n = int(PlayerO.get())
			score = (n+1)
			PlayerO.set(score)
			pb = Player2.get() + " Won the Game!!"
			tkinter.messagebox.showinfo("Tic Tac Toe",pb)
			reset()
		if (button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O"):
			button4.configure(background = '#90ff0a')
			button5.configure(background = '#90ff0a')
			button6.configure(background = '#90ff0a')
			n = int(PlayerO.get())
			score = (n+1)
			PlayerO.set(score)
			pb = Player2.get() + " Won the Game!!"
			tkinter.messagebox.showinfo("Tic Tac Toe",pb)
			reset()
		if (button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O"):
			button7.configure(background = '#90ff0a')
			button8.configure(background = '#90ff0a')
			button9.configure(background = '#90ff0a')
			n = int(PlayerO.get())
			score = (n+1)
			PlayerO.set(score)
			pb = Player2.get() + " Won the Game!!"
			tkinter.messagebox.showinfo("Tic Tac Toe",pb)
			reset()
		if (button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O"):
			button1.configure(background = '#90ff0a')
			button4.configure(background = '#90ff0a')
			button7.configure(background = '#90ff0a')
			n = int(PlayerO.get())
			score = (n+1)
			PlayerO.set(score)
			pb = Player2.get() + " Won the Game!!"
			tkinter.messagebox.showinfo("Tic Tac Toe",pb)
			reset()
		if (button5["text"] == "O" and button2["text"] == "O" and button8["text"] == "O"):
			button5.configure(background = '#90ff0a')
			button2.configure(background = '#90ff0a')
			button8.configure(background = '#90ff0a')
			n = int(PlayerO.get())
			score = (n+1)
			PlayerO.set(score)
			pb = Player2.get() + " Won the Game!!"
			tkinter.messagebox.showinfo("Tic Tac Toe",pb)
			reset()
		if (button6["text"] == "O" and button9["text"] == "O" and button3["text"] == "O"):
			button9.configure(background = '#90ff0a')
			button6.configure(background = '#90ff0a')
			button3.configure(background = '#90ff0a')
			n = int(PlayerO.get())
			score = (n+1)
			PlayerO.set(score)
			pb = Player2.get() + " Won the Game!!"
			tkinter.messagebox.showinfo("Tic Tac Toe",pb)
			reset()
		if (button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O"):
			button1.configure(background = '#90ff0a')
			button5.configure(background = '#90ff0a')
			button9.configure(background = '#90ff0a')
			n = int(PlayerO.get())
			score = (n+1)
			PlayerO.set(score)
			pb = Player2.get() + " Won the Game!!"
			tkinter.messagebox.showinfo("Tic Tac Toe",pb)
			reset()
		if (button5["text"] == "O" and button7["text"] == "O" and button3["text"] == "O"):
			button3.configure(background = '#90ff0a')
			button5.configure(background = '#90ff0a')
			button7.configure(background = '#90ff0a')
			n = int(PlayerO.get())
			score = (n+1)
			PlayerO.set(score)
			pb = Player2.get() + " Won the Game!!"
			tkinter.messagebox.showinfo("Tic Tac Toe",pb)
			reset()
			

def reset():
    button1["text"] = " "
    button2["text"] = " "
    button3["text"] = " "
    button4["text"] = " "
    button5["text"] = " "
    button6["text"] = " "
    button7["text"] = " "
    button8["text"] = " "
    button9["text"] = " "
    
    button1.configure(background = 'white')
    button2.configure(background = 'white')
    button3.configure(background = 'white')
    button4.configure(background = 'white')
    button5.configure(background = 'white')
    button6.configure(background = 'white')
    button7.configure(background = 'white')
    button8.configure(background = 'white')
    button9.configure(background = 'white')

def Newgame():
	global pa,pb,Player1,Player2
	reset()
	PlayerX.set(0)
	PlayerO.set(0)
	Player1 =StringVar()
	Player2 = StringVar()
	
	nmPlayerX= Entry(RightFrame1,font=('arial',40,'bold'),bd=3,fg="black",textvariable= Player1, width=7,
	justify=LEFT).grid(row=0,column=1)
	nmPlayerO=Entry(RightFrame1,font=('arial',40,'bold'),bd=3,fg="black",textvariable= Player2, width=7,
	justify=LEFT).grid(row=1,column=1)



	
lblPlayerX =Label(RightFrame1, font=('arial', 40,'bold'), text="Player X :",padx=2,pady=2, bg="yellow",fg ="black")
lblPlayerX.grid(row=0, column=0,sticky=W)

nmPlayerX= Entry(RightFrame1,font=('arial',40,'bold'),bd=3,fg="black",textvariable= Player1, width=7,
justify=LEFT).grid(row=0,column=1)

txtPlayerX=Button(RightFrame1,font=('arial',26,'bold'),bd=2,fg="black",bg = "yellow",textvariable= PlayerX, width=4,
justify=LEFT).grid(row=0,column=2)
					 
lblPlayerO =Label(RightFrame1, font=('arial', 40,'bold'), text="Player O :",padx=2,pady=2, bg="yellow",fg = "black")
lblPlayerO.grid(row=1, column=0,sticky=W)

nmPlayerO=Entry(RightFrame1,font=('arial',40,'bold'),bd=3,fg="black",textvariable= Player2, width=7,
justify=LEFT).grid(row=1,column=1)

txtPlayerO=Button(RightFrame1,font=('arial',26,'bold'),bd=2,fg="black",bg = "yellow",textvariable= PlayerO, width=4,
justify=LEFT).grid(row=1,column=2)

	
btnReset = Button(RightFrame2, text="Reset", font=('arial', 40,'bold'), height = 1, width=15,fg='white', bg='purple',command = reset)
btnReset.grid(row=1, column=0,padx = 1,pady =11)



btnNewGame = Button(RightFrame2, text="New  Game",  font=('arial', 40,'bold'), height = 1, width=15,fg='white', bg='purple',command = Newgame)
btnNewGame.grid(row=2, column=0,padx = 1, pady =11)

button1 = Button(LeftFrame, text=" ", font=('arial', 30, 'bold'), height = 3, width=8, bg='white', command=lambda:checker(button1))
button1.grid(row=1, column=0, sticky = S+N+E+W)

button2 = Button(LeftFrame, text=" ", font=('arial', 30, 'bold'), height = 3, width=8, bg='white', command=lambda:checker(button2))
button2.grid(row=1, column=1, sticky = S+N+E+W)

button3 = Button(LeftFrame, text=" ", font=('arial',30 ,'bold'), height = 3, width=8, bg='white', command=lambda:checker(button3))
button3.grid(row=1, column=2, sticky = S+N+E+W)

button4 = Button(LeftFrame, text=" ", font=('arial', 30, 'bold'), height = 3, width=8, bg='white', command=lambda:checker(button4))
button4.grid(row=2, column=0, sticky = S+N+E+W)

button5 = Button(LeftFrame, text=" ", font=('arial', 30, 'bold'), height = 3, width=8, bg='white', command=lambda:checker(button5))
button5.grid(row=2, column=1, sticky = S+N+E+W)

button6 = Button(LeftFrame, text=" ", font=('arial', 30, 'bold'), height = 3, width=8, bg='white', command=lambda:checker(button6))
button6.grid(row=2, column=2, sticky = S+N+E+W)

button7 = Button(LeftFrame, text=" ", font=('arial', 30, 'bold'), height = 3, width=8, bg='white', command=lambda:checker(button7))
button7.grid(row=3, column=0, sticky = S+N+E+W)

button8 = Button(LeftFrame, text=" ", font=('arial', 30, 'bold'), height = 3, width=8, bg='white', command=lambda:checker(button8))
button8.grid(row=3, column=1, sticky = S+N+E+W)

button9 = Button(LeftFrame, text=" ", font=('arial', 30, 'bold'), height = 3, width=8, bg='white', command=lambda:checker(button9))
button9.grid(row=3, column=2, sticky = S+N+E+W)

root.mainloop()