"""
Tired of ads and website downloader, so this script came to mind.
Basically, it takes the Youtube URL of the video and dowload the highest available resolution using pytube library

Requirements:
- pytube 
"""

# Importing the library
from pytube import YouTube
from pytube.cli import on_progress

def VideoDowload(youtubeObject):
    """ Function to download video with the highest available resolution. """
    youtubeObjectStream = youtubeObject.streams.get_highest_resolution()
    try:
        video_title = youtubeObject.title
        print("Donwloading video: %s ...." % video_title)
        youtubeObjectStream.download()
    except:
        print("Oops ... Something is wrong...")
    print("\n Download is completed successfully.")

def mp3Downloader(link):
    """ Function to extact audio from an YouTube Video. """
    


if __name__ == '__main__':
    link = input("Copy here the YouTube video URL: \n>> ")
    youtubeObject = YouTube(link, 
                        on_progress_callback=on_progress)
    VideoDowload(youtubeObject)