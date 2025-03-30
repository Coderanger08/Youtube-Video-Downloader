import yt_dlp
import tkinter as tk
from tkinter import filedialog
import os

def download_video(url, save_path):
    try:
        ydl_opts = {
            'format': 'mp4',  # Download the best video and audio
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',  # Save with the video title
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Video downloaded successfully to {save_path}")

    except Exception as e:
        print(f"An error occurred: {e}")
"""
# Cleaned URL (full YouTube URL)
url = "https://www.youtube.com/watch?v=LUttsadgSEY"  # Full URL

# Save path is set to the current working directory (where the script is located)
save_path = os.getcwd()  # Get the current working directory

# Call the function
download_video(url, save_path)
"""

def open_file_dialog():
    folder=filedialog.askdirectory() # Open a dialog to select a folder
    if folder:
        print(f"Selected folder: {folder}")
    return folder


if __name__ == "__main__": # Main function to run the script
    root=tk.Tk() #instantiate the Tk class/ window
    root.withdraw() #hide the root window

    #these code will run when we directly run this exact script

    video_url=input("Enter the YouTube video URL: ") #prompt user for the video URL
    save_dir=open_file_dialog() #call the function to open file dialog and get the folder path

    if not save_dir:
        print("Invalid save location. Please select a valid folder.")
    else:
        download_video(video_url, save_dir)
        print("Started Download")