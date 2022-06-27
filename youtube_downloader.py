from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil

def select_path():
    #allows user to select path from explorer
    path=filedialog.askdirectory()
    path_label.config(text=path)

def download_file():
    #get user path
    get_link=link_field.get()
    #get selected_path
    user_path=path_label.cget("text")
    screen.title("Downloading.......")
    #download video
    mp4_video=YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip=VideoFileClip(mp4_video)
    vid_clip.close()
    #move file to selected directory
    shutil.move(mp4_video,user_path)
    screen.title("Download Complete! Downloaded to user floder...")

screen=Tk()
screen.title("Youtube video downloader application")
canvas=Canvas(screen,width=500,height=500)
# The canvas widget is used to add the structured graphics to the python application.
canvas.pack()

#image logo
logo_img=PhotoImage(file='yt.png')
#resize
logo_img=logo_img.subsample(2,2)
canvas.create_image(250,80,image=logo_img)

#linked field
link_field=Entry(screen,width=40,font=('Arial',15))
link_label=Label(screen,text="Enter Download link: ",font=('Arial',15))

#selected path for saving the file
path_label=Label(screen,text="Select path for Download",font=('Arial',15))
select_btn=Button(screen,text="Select path",bg='red',padx='22',pady='5',font=('Arial',15),fg='#fff',command=select_path)

#add to window
canvas.create_window(250,280,window=path_label)
canvas.create_window(250,330,window=select_btn)

#add widgets to window
canvas.create_window(250,170,window=link_label)
canvas.create_window(250,280,window=link_field)

#Download btns
download_btn=Button(screen,text="Download file",bg='green',padx='22',pady='5',font=('Arial',15),fg='#fff',command=download_file)

# add to canvas
canvas.create_window(250,390,window=download_btn)

screen.mainloop()
