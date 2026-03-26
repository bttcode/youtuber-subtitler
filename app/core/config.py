import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    EMAIL_SENDER = os.getenv("EMAIL_SENDER")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
    FFMPEG_PATH = r'D:\Projects\youtube_subtitler\ffmpeg\bin'
    DOWNLOAD_FOLDER = 'downloads'

settings = Settings()