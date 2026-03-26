from flask import Blueprint, request, jsonify
from app.services.youtube import download_audio
from app.services.ai_service import process_subtitles
from app.services.mail import send_email
import os

webhook_bp = Blueprint('webhook', __name__)

@webhook_bp.route('/webhook', methods=['POST'])
def handle_webhook():
    data = request.json
    email = data.get('email')
    url = data.get('url')

    try:
        # Step 1: Download
        audio_file = download_audio(url)
        
        # Step 2: AI Process
        vietnamese_srt = process_subtitles(audio_file)
        
        # Step 3.1: Save file temporarily
        output_path = "translated_sub.srt"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(vietnamese_srt)
            
        # Step 3.2: Send email
        send_email(
            subject="[Auto-Sub] Your subtitles are ready!",
            body=f"Hello, the system has finished translating the video: {url}",
            attachment_path=output_path,
            recipient_email=email
        )
        
        return jsonify({"status": "success", "message": "Sent subtitles successfully!"}), 200

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500
    
    finally:
        if audio_file and os.path.exists(audio_file):
            os.remove(audio_file)
        if os.path.exists(output_path):
            os.remove(output_path)