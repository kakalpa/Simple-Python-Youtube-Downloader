import customtkinter
import tkinter
from pytube import YouTube
from tkinter import filedialog
import webbrowser

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("720x500")
app.title("Youtube Downloader")
app.resizable(False, False)

#logic

def getVideoInfo():
    try:
        ytlink = link_var.get()
        yt = YouTube(ytlink, on_progress_callback=onProgress)
        video_Title = yt.title
        videoLength = yt.length/60.00
        videoTitleText.configure(text="Title : "+video_Title,text_color = "blue")
        videolenToText = str(int(videoLength))
        videolenthText.configure(text="Length : "+str(videolenToText)+" Minutes", text_color = "blue")  
    except Exception as e:
        videoTitleText.configure(text=f"Error Occurd Please Check the URL", text_color = "red")
        


def downloadVideo():
    try:
        ytlink = link_var.get()
        videoTitleText.configure(text="")
        yt = YouTube(ytlink, on_progress_callback=onProgress)
        if quality_var in ["144p", "240p", "360p", "480p", "720p", "1080p"]:
            video = yt.streams.get_by_resolution(quality_var)
            folder_path = filedialog.askdirectory()
            video.download(folder_path,video.title+".mp4")
            downloadQText.configure(text="Video Downloaded Successfully", text_color = "green")
        else:
            downloadQText.configure(text="No Quality Selected Downloading the Highest Possible Quality", text_color = "Yellow")
            video = yt.streams.get_highest_resolution()
            folder_path = filedialog.askdirectory()
            video.download(folder_path,video.title+".mp4")
            downloadQText.configure(text="Video Downloaded Successfully", text_color = "green")
    except Exception as e:
        downloadQText.configure(text=e, text_color = "red")
        
def onProgress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    presentage = str(int(percentage_of_completion))
    progress_presentage.configure(text=presentage+"%")
    progress_presentage.update()
    progress_bar.set(percentage_of_completion/100)

def callback(url):
    webbrowser.open_new(url)
    
    



# Designing the UI 

title = customtkinter.CTkLabel(app, text="Youtube link here", font=("Arial", 20))
title.pack(pady=10, padx=10)

#input

link_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=500, height=40, font=("Arial", 20), textvariable=link_var)
link.pack()

getinfo_button = customtkinter.CTkButton(app, text="Get Video Info", command=getVideoInfo, font=("Arial", 20))
getinfo_button.pack(pady=10, padx=10)


videoTitleText = customtkinter.CTkLabel(app, text="", font=("Arial", 20))
videoTitleText.pack(pady=10, padx=10)

videolenthText = customtkinter.CTkLabel(app, text="", font=("Arial", 20))
videolenthText.pack(pady=10, padx=10)

# progress presentage

progress_presentage = customtkinter.CTkLabel(app, text="")
progress_presentage.pack(pady=10, padx=10)

progress_bar = customtkinter.CTkProgressBar(app, width=400)
progress_bar.set(0)
progress_bar.pack(pady=10, padx=10)


downloadQText = customtkinter.CTkLabel(app, text="Select the Video Quality to Download", font=("Arial", 10))
downloadQText.pack(pady=20, padx=10)


# Video QUality selector drop down 

quality_var = tkinter.StringVar()
video_quality = customtkinter.CTkOptionMenu(app, values=["144p", "240p", "360p", "480p", "720p", "1080p"], variable=quality_var)
video_quality.pack(pady=5, padx=10)

# Download button

download_button = customtkinter.CTkButton(app, text="Download Video", command=downloadVideo, font=("Arial", 20))
download_button.pack(pady=10, padx=10)

git_link = customtkinter.CTkLabel(app, text="to my GIT-Hub", font=("Arial", 10), cursor="hand2")
git_link.pack(pady=10, padx=10)
git_link.bind("<Button-1>", lambda e: callback("https://github.com/kakalpa"))

app.mainloop()
