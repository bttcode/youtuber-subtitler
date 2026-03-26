from openai import OpenAI
from app.core.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def process_subtitles(audio_path):
    with open(audio_path, "rb") as audio:
        transcript_srt = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio, 
            language="ko",
            response_format="srt"
        )
    print("Transcription completed. Starting translation...")
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an expert subtitle translator."},
            {"role": "user", "content": f"Translate this Korean SRT subtitle file to Vietnamese. Keep the timestamp format unchanged. Please provide a natural, accurate translation:\n\n{transcript_srt}"}
        ]
    )
    print("Translation completed.")
    return response.choices[0].message.content