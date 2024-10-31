import yt_dlp
import tkinter as tk
from tkinter import messagebox
import threading

download_thread = None
should_stop = False

def download_playlist():
    global should_stop

    playlist_url = url_entry.get()
    if not playlist_url:
        messagebox.showwarning("Input Error", "Please enter a playlist URL.")
        return
    
    should_stop = False

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ffmpeg_location': r'D:\ffmpeg\bin', 
        'outtmpl': '%(title)s.%(ext)s',  
        'progress_hooks': [hook],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
        messagebox.showinfo("Success", "All audio files downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Download Error", str(e))

def hook(d):
    if d['status'] == 'finished':
        speed_var.set("Speed: --")
        progress_var.set(0)  
    elif d['status'] == 'downloading':
        if should_stop:
            d['status'] = 'finished' 
            return
        speed = d.get('speed', 0)
        speed_var.set(f"Speed: {speed / 1_000:.2f} kB/s") 
        
        downloaded_bytes = d.get('downloaded_bytes', 0)
        total_bytes = d.get('total_bytes', 0)
        if total_bytes:
            progress = (downloaded_bytes / total_bytes) * 100
            progress_var.set(progress)

def stop_download():
    global should_stop
    should_stop = True
    messagebox.showinfo("Stopped", "Download has been stopped.")

def start_download_thread():
    global download_thread
    download_thread = threading.Thread(target=download_playlist)
    download_thread.start()

app = tk.Tk()
app.title("YouTube Playlist Downloader")

url_label = tk.Label(app, text="Enter Playlist URL:")
url_label.pack(pady=10)

url_entry = tk.Entry(app, width=50)
url_entry.pack(pady=10)

speed_var = tk.StringVar(value="Speed: --")  # Initialize with placeholder
speed_label = tk.Label(app, textvariable=speed_var)
speed_label.pack(pady=10)

progress_var = tk.DoubleVar()
progress_bar = tk.Scale(app, variable=progress_var, from_=0, to=100, orient=tk.HORIZONTAL)
progress_bar.pack(pady=10)

download_button = tk.Button(app, text="Download", command=start_download_thread)
download_button.pack(pady=10)

stop_button = tk.Button(app, text="Stop", command=stop_download)
stop_button.pack(pady=10)

app.mainloop()
