import smtplib
import os
from email.message import EmailMessage
from app.core.config import settings

def send_email(subject, body, attachment_path, recipient_email):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = settings.EMAIL_SENDER
    msg['To'] = recipient_email
    msg.set_content(body)

    with open(attachment_path, 'rb') as f:
        file_data = f.read()
        file_name = os.path.basename(attachment_path)
        msg.add_attachment(
            file_data, 
            maintype='application', 
            subtype='octet-stream', 
            filename=file_name
        )

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(settings.EMAIL_SENDER, settings.EMAIL_PASSWORD)
        smtp.send_message(msg)
    
    print(f"--- Sent email to {recipient_email} successfully! ---")