import yt_dlp

playlist_url = "https://www.youtube.com/playlist?list=PLeBcC5rsXI6ZgzVQIRJHAjHhyXLKMLqHM"

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'ffmpeg_location': r'D:\ffmpeg\bin', 
    'outtmpl': '%(title)s.%(ext)s',  
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])

print("All audio files downloaded successfully!")
