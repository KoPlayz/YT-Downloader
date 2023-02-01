import youtube_dl
import datetime
import os
import tkinter as tk
from tkinter import filedialog

def download_video(video_url, download_path):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'noplaylist': False,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=True)

    title = info_dict.get('title', '')
    description = info_dict.get('description', '')
    uploader = info_dict.get('uploader', '')
    date = datetime.datetime.fromtimestamp(int(info_dict.get('upload_date', ''))).strftime('%Y-%m-%d %H:%M:%S')

    with open(os.path.join(download_path, f"{title}.txt"), "w") as f:
        f.write(f"Title: {title}\n")
        f.write(f"Description: {description}\n")
        f.write(f"Uploader: {uploader}\n")
        f.write(f"Upload date: {date}\n")

if __name__ == "__main__":
    video_url = input("Enter the URL of the video, playlist, or channel: ")
    root = tk.Tk()
    root.withdraw()
    download_path = filedialog.askdirectory(title = "Select the download folder")
    download_video(video_url, download_path)
