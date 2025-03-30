# YouTube Video Downloader

## Overview

The **YouTube Video Downloader** is a simple Python script that automates the process of downloading YouTube videos. It eliminates the hassle of using third-party software or web services to download videos. With this project, users can quickly input a YouTube video URL and select a directory to save the video in MP4 format. The goal of this project was to streamline the video download process and make it easily accessible.

## Motivation

Downloading videos from YouTube often requires third-party software or online services, which can be time-consuming and sometimes unreliable. I wanted to automate this process, making it more efficient, seamless, and customizable. After facing difficulties with existing tools, I decided to build my own video downloader with Python.

This project was created to simplify the YouTube video downloading experience and eliminate the need for external software. It allows users to easily download videos with just a few clicks.

## Features

- **Simple User Interface**: The program uses `Tkinter` for an easy-to-use file dialog for selecting the download location.
- **Download Videos in MP4 Format**: The script downloads the video in the best available MP4 format.
- **Customizable Save Location**: Users can choose where they want the video to be saved on their local machine.
- **Automated Process**: The script automates the entire process, so you don’t have to worry about navigating through third-party software.

## Installation

### Prerequisites

Before running this script, make sure you have Python installed on your system (preferably Python 3.x). You will also need to install the required libraries:

1. **yt-dlp**: A powerful tool for downloading videos from YouTube and other sites.
2. **Tkinter**: A Python library for building simple graphical user interfaces (GUIs).

### Installation Steps

1. **Install Python dependencies**:
   To install the required libraries, run the following command in your terminal or command prompt:

   ```bash
   pip install yt-dlp
   ```

2. **Run the script**:
   You can run the script by executing it in your terminal or command prompt. Simply navigate to the directory containing the script and run:

   ```bash
   python youtube_video_downloader.py
   ```

## How to Use

1. **Run the script**: Once the script is executed, it will prompt you to input the YouTube video URL.
2. **Select a save location**: A file dialog will open for you to choose where to save the downloaded video.
3. **Start the download**: After selecting the directory, the video will begin downloading automatically.

The video will be saved in MP4 format in the folder you selected.

## Example Usage

```bash
Enter the YouTube video URL: https://www.youtube.com/watch?v=LUttsadgSEY
Selected folder: C:/Users/YourName/Downloads
Video downloaded successfully to C:/Users/YourName/Downloads
```

## How It Works

1. The user inputs the YouTube video URL.
2. The program opens a file dialog, allowing the user to select the destination folder.
3. Using the **yt-dlp** library, the script downloads the video in MP4 format, saving it to the chosen location.
4. Once the download is complete, the user receives a message confirming the successful download.

## Acknowledgements

- **YouTube Tutorial**: I took inspiration from various YouTube tutorials to learn how to automate the YouTube video downloading process using Python. Special thanks to the open-source community for making tutorials and sharing their knowledge.
- **yt-dlp**: This powerful Python library helped me achieve my goal of downloading YouTube videos in a seamless manner.

## License

This project is open-source and available under the [MIT License](LICENSE).