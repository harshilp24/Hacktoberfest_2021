
from pytube import YouTube
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter import *
from threading import *

root = Tk()
root.title("Youtube video downloader")
#path of icon should be added here
root.iconbitmap("...")
root.geometry("550x650")

#for creating a constant  gui window
root.resizable(width=0 ,height=0)

font = ('Helvetica', 20)
file_size = 0



def completeDownload(stream=None, file_path=None):
    print("download completed")
    showinfo("Message", "Successfuly,downloaded the file.")
    downloadBtn['text'] = "Download Video"
    downloadBtn['state'] = "active"
    urlField.delete(0, END)



def progressDownload(stream=None, chunk=None, bytes_remaining=None):
    percent = (100 * ((file_size - bytes_remaining) / file_size))
    downloadBtn['text'] = "{:00.0f}% downloaded ".format(percent)



def startDownload(url):
    global file_size
    path_to_save = askdirectory()
    if path_to_save is None:
        return

    try:
        yt = YouTube(url)
        st = yt.streams.first()

        yt.register_on_complete_callback(completeDownload)
        yt.register_on_progress_callback(progressDownload)

        file_size = st.filesize
        st.download(output_path=path_to_save)

    except Exception as e:
        print(e)
        


def btnClicked():
    try:
        downloadBtn['text'] = "Please wait..."
        downloadBtn['state'] = 'disabled'
        url = urlField.get()
        if url == '':
            return
        print(url)
        
        # to avoid interruption between the display and functioning of the downloader
        thread = Thread(target=startDownload, args=(url,))
        thread.start()

    except Exception as e:
        print(e)
        print("something went wrong,try again")


#add image path to add in the gui window
file = PhotoImage(file="....")
headingIcon = Label(root, image=file)
headingIcon.pack(side=TOP, pady=3)

# making url field
urlField = Entry(root, font=font, justify=CENTER)
urlField.pack(side=TOP, fill=X, padx=10)
urlField.focus()

# download button
downloadBtn = Button(root, text="Download Video", font=font, relief='solid', command=btnClicked)
downloadBtn.pack(side=TOP, pady=20)

root.mainloop()
