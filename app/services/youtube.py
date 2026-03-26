import yt_dlp
import os
from app.core.config import settings

def download_audio(youtube_url):
    if not os.path.exists(settings.DOWNLOAD_FOLDER):
        os.makedirs(settings.DOWNLOAD_FOLDER)
        
    file_path = os.path.join(settings.DOWNLOAD_FOLDER, 'audio_input')
    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        'outtmpl': file_path,
        'noplaylist': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
        'ffmpeg_location': settings.FFMPEG_PATH,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])
    return f"{file_path}.mp3"