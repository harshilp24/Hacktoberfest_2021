from tkinter import *
import os
from tkinter import messagebox as msg
import tkinter.filedialog as log


window = Tk()
window.geometry("600x400")
window.title("untitled - Notepad")
# window.wm_iconbitmap("Notepad.ico")

# variables
menu_index = IntVar()
name = ""


# functions
def menu(event):
    global menu_index
    index = window.call(event.widget, "index", "active")
    if index != "none":
        menu_index.set(index)


def background():
    a = True
    while a:
        index = menu_index.get()
        if index == 0:
            note.configure(bg="White")
        elif index == 1:
            note.configure(bg="Blue")
        elif index == 2:
            note.configure(bg="Yellow")
        elif index == 3:
            note.configure(bg="Green")
        elif index == 4:
            note.configure(bg="Pink")

        window.wait_variable(menu_index)
        background()


def new():
    global file
    file = None
    note.delete(1.0, END)


def opening():
    global file
    global name
    fil = log.askopenfilename(defaultextension=".txt",
                              filetypes=[("All files", "*.*"), ("Text Document", "*.txt")])

    name = fil
    if fil == "":
        file = None

    else:
        window.title(os.path.basename(fil) + " - Notepad")
        note.delete(1.0, END)
        with open(fil, "r") as f:
            note.insert(1.0, f.read())


def save_as():
    global file
    file = log.asksaveasfilename(initialfile="Untitled.txt",
                                 defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"), ("Text Document", "*.txt")])

    if file == "":
        file = None
    else:
        with open(file, "w") as f:
            f.write(note.get(1.0, END))

        window.title(os.path.basename(file) + " - Notepad")
        msg.Message("File Saved")


def save():
    global name
    try:
        with open(name, "w") as f:
            f.write(note.get(1.0, END))

        window.title(os.path.basename(name) + " - Notepad")
        print(name)
    except:
        save_as()


def cut():
    note.event_generate("<<Cut>>")


def copy():
    note.event_generate("<<Copy>>")


def paste():
    note.event_generate("<<Paste>>")


def undo():
    note.edit_undo()


def redo():
    note.edit_redo()


def about():
    msg.showinfo("About Us", "We are a developer company from INDIA.\nMaking software for smoother life.")


def donate():
    msg.showinfo("Donate Us", "We are providing these types\n "
                              "of free software for you.\n "
                              "Would you like to buy a cup\n "
                              "of coffee for the developer.\n ThankYou")


# start of Menubar

mainmenu = Menu(window)

File = Menu(mainmenu, tearoff=0, activebackground="cyan")
File.add_cascade(label="New", command=new)
File.add_cascade(label="Open", command=opening)
File.add_cascade(label="Save", command=save)
File.add_cascade(label="Save As", command=save_as)
File.add_separator()
File.add_cascade(label="Quit", command=window.destroy)
mainmenu.add_cascade(label="File", menu=File)

Edit = Menu(mainmenu, tearoff=0, activebackground="cyan")
Edit.add_cascade(label="Undo", command=undo)
Edit.add_cascade(label="Redo", command=redo)
Edit.add_separator()
Edit.add_cascade(label="Cut", command=cut)
Edit.add_cascade(label="Copy", command=copy)
Edit.add_cascade(label="Paste", command=paste)
mainmenu.add_cascade(label="Edit", menu=Edit)

Font = Menu(mainmenu, tearoff=0, activebackground="cyan")
Font.add_command(label="White")
Font.add_command(label="Blue")
Font.add_command(label="Yellow")
Font.add_command(label="Green")
Font.add_command(label="Pink")
mainmenu.add_cascade(label="Font", menu=Font)

Help = Menu(mainmenu, tearoff=0, activebackground="cyan")
Help.add_cascade(label="Help", command=help)
Help.add_cascade(label="About", command=about)
mainmenu.add_cascade(label="Help", menu=Help)

# Donate
mainmenu.add_cascade(label="Donate Us", command=donate)

Font.bind("<<MenuSelect>>", menu)
window.config(menu=mainmenu)

# end of menubar


# start of textarea

note = Text(window, undo=True)
file = None
note.pack(expand=True, fill=BOTH)

# end of textarea


# scrollbar
scroll = Scrollbar(note)
scroll.pack(side=RIGHT,  fill=Y)
scroll.config(command=note.yview)
note.config(yscrollcommand=scroll.set)

background()
window.mainloop()
