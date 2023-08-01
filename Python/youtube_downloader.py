"""
Tired of ads and website downloader, so this script came to mind.
Basically, it takes the Youtube URL of the video and dowload the highest available resolution using pytube library

Requirements:
- pytube 
"""

# Importing the library
from pytube import YouTube

def VideoDowload(link):
    """ Function to download video with the highest available resolution """
    youtubeObject = YouTube(link)
    youtubeObjectStream = youtubeObject.streams.get_highest_resolution()
    try:
        print("Donwloading ....")
        youtubeObjectStream.download()
    except:
        print("Oops ... Something is wrong...")
    print("Download is completed successfully")

link = input("Copy here the YouTube video URL: ")
VideoDowload(link)