from pytube import *
from tkinter.filedialog import *
from tkinter import *
from tkinter.messagebox import *
from threading import *
from tkinter.ttk import *

file_size = 0
choice = []
#updating %
def progress(stream,chunk:bytes,bytes_remaining:int):
    #getting %

    file_downloaded = (file_size-bytes_remaining)
    per= (file_downloaded/file_size)*100
    dBtn.config(text="{:00.0f} % Downloaded".format(per))

#Downloading
def startDownload():
    global file_size
    try:
        #getting url
        #url = "https://www.youtube.com/watch?v=hip-_JbR888"
        url = urlField.get()
        print(url)
       
    
        dBtn.config(text='Please wait..')
        dBtn.config(state=DISABLED)
        #formation of stream object
        ob= YouTube(url,on_progress_callback=progress)
        Title = ob.streams.first()
        strms= ob.streams

        actual_streams = {}
        for s in strms:
            a= str(s.filesize)
            b= str(s)
            c=list(b.split(" "))
            d= c[2]
            e=c[3]
            value = str(e+" "+d+" "+a+"bytes")
            actual_streams.update({value:s})
            choice.append(value)
    
        vTitle.config(text=Title.title)
        vTitle.pack(side=TOP)
        
        combo = Combobox(main, values= choice , width= 30 )
        combo.pack(side=TOP,pady=5)

        my_stream=combo.get()
        while (my_stream==""):
            my_stream=combo.get()
       
        path_to_save_video = askdirectory() 
        print(path_to_save_video)
        if path_to_save_video is None:
            return

        strm=actual_streams[my_stream]
        file_size=strm.filesize
        print(file_size)

        '''print(strm)
        print(strm.filesize)
        print(strm.title)'''
        strm.download(path_to_save_video)
        print("done...")
        dBtn.config(text='Start Download')
        dBtn.config(state=NORMAL)
        showinfo("Download Finished","Downloaded succesfully")
        urlField.delete(0,END)
        vTitle.pack_forget()
        
    except Exception as e:
        print(e)
        print("error !!")
        showinfo("Invalid URL","Please enter correct URL")
        urlField.delete(0,END)
        dBtn.config(text="Start Download")
        dBtn.config(state=NORMAL)
        
def startDownloadThread():
    thread = Thread(target=startDownload)
    thread.start()
main = Tk()
main.title("My YouTube Downloader")

#setting icon
main.iconbitmap('.\\res\\icon.ico')

main.geometry("500x600")

#heading icon
file = PhotoImage(file='.\\res\\youtube.png')
headingIcon = Label(main,image=file)
headingIcon.pack(side=TOP)
#url textfield
urlField = Entry(main,font=("verdana",18),justify=CENTER)
urlField.pack(side=TOP,fill=X,padx=10)
#dwnld button

dBtn = Button(main,text="Start Download", command=lambda:startDownloadThread())
dBtn.pack(side=TOP,pady=10)

#title
vTitle = Label(main,text="Video Title")
vTitle.pack(side=TOP)


main.mainloop()

