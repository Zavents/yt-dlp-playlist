import yt_dlp
import tkinter as tk
from tkinter import messagebox
import threading

# Global variable to control download
download_thread = None
should_stop = False

def download_playlist():
    global should_stop

    playlist_url = url_entry.get()
    if not playlist_url:
        messagebox.showwarning("Input Error", "Please enter a playlist URL.")
        return
    
    # Reset stop flag
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
        # Reset speed display when finished
        speed_var.set("Speed: --")
        progress_var.set(0)  # Reset progress bar
    elif d['status'] == 'downloading':
        if should_stop:
            d['status'] = 'finished'  # Stop the download
            return
        speed = d.get('speed', 0)
        # Only display speed
        speed_var.set(f"Speed: {speed / 1_000:.2f} kB/s")  # Display speed in kB/s

        # Optionally, update the progress bar if you want to keep track of progress
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

# Setting up the GUI
app = tk.Tk()
app.title("YouTube Playlist Downloader")

# URL Label
url_label = tk.Label(app, text="Enter Playlist URL:")
url_label.pack(pady=10)

# URL Entry
url_entry = tk.Entry(app, width=50)
url_entry.pack(pady=10)

# Speed Display
speed_var = tk.StringVar(value="Speed: --")  # Initialize with placeholder
speed_label = tk.Label(app, textvariable=speed_var)
speed_label.pack(pady=10)

# Progress Display
progress_var = tk.DoubleVar()
progress_bar = tk.Scale(app, variable=progress_var, from_=0, to=100, orient=tk.HORIZONTAL)
progress_bar.pack(pady=10)

# Download Button
download_button = tk.Button(app, text="Download", command=start_download_thread)
download_button.pack(pady=10)

# Stop Button
stop_button = tk.Button(app, text="Stop", command=stop_download)
stop_button.pack(pady=10)

# Run the GUI event loop
app.mainloop()
