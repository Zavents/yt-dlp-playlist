# YouTube Playlist Downloader

## Overview

This application allows users to download audio files from YouTube playlists easily. It uses `yt-dlp` for downloading and `Tkinter` for the graphical user interface.

## Prerequisites

Before you can run the YouTube Playlist Downloader, you need to install the following:

### 1. Python

Make sure you have Python installed on your system. You can download it from the official website:

- [Download Python](https://www.python.org/downloads/)

### 2. FFmpeg

FFmpeg is required for audio conversion. Follow these steps to install FFmpeg:

- **Windows:**
  1. Download the FFmpeg build for Windows from [FFmpeg Downloads](https://ffmpeg.org/download.html#build-windows).
  2. Extract the downloaded ZIP file.
  3. Move the extracted folder (e.g., `ffmpeg-2024-xx-xx-xxxx-full_build`) to `C:\` or any preferred directory.
  4. Add FFmpeg to your system PATH:
     - Right-click on "This PC" or "My Computer" and select "Properties."
     - Click on "Advanced system settings."
     - Click on the "Environment Variables" button.
     - Under "System variables," find the `Path` variable and click "Edit."
     - Add the path to the `bin` folder inside the extracted FFmpeg folder (e.g., `C:\ffmpeg-2024-xx-xx-xxxx-full_build\bin`).
     - Click "OK" to close all dialog boxes.

- **Mac:**
  ```bash
  brew install ffmpeg
  ```

- **Linux:**
  ```bash
  sudo apt update
  sudo apt install ffmpeg
  ```

### 3. Required Python Modules

You need to install the `yt-dlp` and `tkinter` modules. You can install `yt-dlp` using pip:

```bash
pip install yt-dlp
```

### Note on Tkinter

`Tkinter` usually comes pre-installed with Python on Windows and macOS. If you’re using Linux, you may need to install it manually. Use the following command if it's not available:

- **Ubuntu/Debian:**
  ```bash
  sudo apt-get install python3-tk
  ```

## Usage

1. **Clone or Download the Repository:**

   If you're using Git, you can clone the repository:

   ```bash
   git clone <repository-url>
   cd youtube_playlist_downloader
   ```

   Or simply download the ZIP file and extract it.

2. **Run the Application:**

   If you have installed Python and the necessary modules, you can run the application directly from the terminal:

   ```bash
   python youtube_downloader.py
   ```

   If you have an executable file (`youtube_downloader.exe`), you can double-click it to run the application.

3. **Using the Application:**

   - Open the application.
   - Enter the YouTube playlist URL in the provided field.
   - Click the "Download" button to start downloading.
   - The application will display the current download speed and progress.
   - You can click the "Stop" button to cancel the download.

## Troubleshooting

- If you encounter issues with downloading, ensure that you have the correct URL format for the YouTube playlist.
- Check that FFmpeg is correctly installed and added to your PATH.
- Ensure you have an active internet connection.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
