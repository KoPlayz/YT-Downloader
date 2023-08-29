import yt_dlp as youtube_dl
import datetime
import os
import tkinter as tk
from tkinter import filedialog

def download_video(video_url, download_path, quality='1080p'):
    try:
        ydl_opts = {
            'format': f'bestvideo[ext=mp4][height<={quality}]+bestaudio[ext=m4a]/best[ext=mp4][height<={quality}]/best',
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
    except youtube_dl.utils.DownloadError as e:
        print(f"DownloadError: {e}")
    except Exception as e:
        print(f"Error: {e}")



if __name__ == "__main__":
    root = tk.Tk()
    root.title("YT-Downloader")

    tk.Label(root, text="URL:").grid(row=0, column=0, padx=10, pady=10)
    url_entry = tk.Entry(root, width=60)
    url_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

    tk.Button(root, text="Output", command=lambda: output_path_entry.delete(0, tk.END) or output_path_entry.insert(0, filedialog.askdirectory(title = "Select the download folder"))).grid(row=1, column=0, padx=10, pady=10)
    output_path_entry = tk.Entry(root, width=60)
    output_path_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

    tk.Button(root, text="Go!", bg="green", width=20, height=2, command=lambda: download_video(url_entry.get(), output_path_entry.get(), resolution_var.get())).grid(row=2, column=1, columnspan=2, padx=10, pady=10)


    status_label = tk.Label(root, text="", fg="black")
    status_label.grid(row=3, column=1, columnspan=2, padx=10, pady=10)
    
    tk.Label(root, text="Video Resolution:").grid(row=4, column=0, padx=10, pady=10)
    resolution_var = tk.StringVar(root)
    resolution_var.set("1080p")  # default value
    resolution_options = ["4K", "2K", "1080p", "720p", "480p", "360p", "240p"]
    resolution_dropdown = tk.OptionMenu(root, resolution_var, *resolution_options)
    resolution_dropdown.grid(row=4, column=1, padx=10, pady=10)

    root.mainloop()