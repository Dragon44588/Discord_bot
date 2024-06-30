import json
from yt_dlp import YoutubeDL

def lookup_video(term, title):
    #determines the options for downloading the song
    ydl_opts = {
    'format': 'm4a/bestaudio/best',
    'download_archive': 'songs.txt',
    'postprocessors': [{  # Extract audio using ffmpeg
    'key': 'FFmpegExtractAudio',
    'preferredcodec': 'm4a'
    }],
    'outtmpl': title+'.%(ext)s',
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(term, download=False)
        error_code = ydl.download(term) 