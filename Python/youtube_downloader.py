"""
Tired of ads and website downloader, so this script came to mind.
Basically, it takes the Youtube URL of the video and dowload the highest available resolution using pytube library.

Also a new function for downloading an MP3 has been added. 

Requirements:
- pytube 

Be mindfull of the Copyrights ©️. 
"""

# Importing the library
from pytube import YouTube
from pytube.cli import on_progress
import os

def videoDowloader(youtubeObject, video_title):
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
    #audio_stream = youtubeObject.streams.filter(only_audio = True).first()
    audio_stream = youtubeObject.streams.get_audio_only()
    try:
        print("\n Extacting audio from a YouTube video: %s ...." % video_title)
        audio = audio_stream.download()         # Download the file
        base, ext = os.path.splitext(audio)    # Save to a file
        new_audio_file =  base + '.mp3'
        os.rename(audio, new_audio_file)
    except:
        print("Oops ... Something is wrong...")
    print("\n Download is completed successfully.")

def tasks(choix, youtubeObject, video_title):
    """ Function for the dowload. """
    if choix == 1:
        # For downloading MP3
        mp3Downloader(youtubeObject, video_title)
    elif choix == 2:
        # For downloading video with the highest available resolution 
        videoDowloader(youtubeObject, video_title)
    elif choix == 3:
        mp3Downloader(youtubeObject, video_title)
        videoDowloader(youtubeObject, video_title)

if __name__ == '__main__':
    link = input("Copy here the YouTube video URL: \n>> ")
    youtubeObject = YouTube(link, 
                        on_progress_callback=on_progress)
    video_title = youtubeObject.title
    
    choix = int(input("What do you want to donwload? \n 1. Audio\n 2. Video\n 3. Both\n >>  "))

    if choix in [1, 2, 3]:
        tasks(choix, youtubeObject, video_title)
    else:
        print("Goddamn it. Choose from the number: 1 or 2 or 3.")
        choix = int(input("What do you want to donwload? \n 1. Audio\n 2. Video\n 3. Both\n >>  "))
        tasks(choix, youtubeObject, video_title)