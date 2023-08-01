"""
Tired of ads and website downloader, so this script came to mind.
Basically, it takes the Youtube URL of the video and dowload the highest available resolution using pytube library

Requirements:
- pytube 
"""

# Importing the library
from pytube import YouTube
from pytube.cli import on_progress
import os

def VideoDowload(youtubeObject, video_title):
    """ Function to download video with the highest available resolution. """
    youtubeObjectStream = youtubeObject.streams.get_highest_resolution()
    try:
        print("\n Donwloading video: %s ...." % video_title)
        youtubeObjectStream.download()
    except:
        print("Oops ... Something is wrong...")
    print("\n Download is completed successfully.")

def mp3Downloader(youtubeObject, video_title):
    """ Function to extact audio from an YouTube Video. """
    audio_stream = youtubeObject.streams.filter(only_audio = True).first()
    try:
        print("\n Extacting audio from a YouTube video: %s ...." % video_title)
        audio = audio_stream.download()         # Download the file
        base, ext = os.path.splitext(audio)    # Save to a file
        new_audio_file =  base + '.mp3'
        os.rename(audio, new_audio_file)
    except:
        print("Oops ... Something is wrong...")
    print("\n Download is completed successfully.")

if __name__ == '__main__':
    link = input("Copy here the YouTube video URL: \n>> ")
    youtubeObject = YouTube(link, 
                        on_progress_callback=on_progress)
    video_title = youtubeObject.title
    
    # For downloading MP3
    mp3Downloader(youtubeObject, video_title)

    # For downloading video with the highest available resolution 
    VideoDowload(youtubeObject, video_title)