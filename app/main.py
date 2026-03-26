from flask import Flask
from app.api.webhook import webhook_bp
from app.core.config import settings
import os

def create_app():
    app = Flask(__name__)

    if not os.path.exists(settings.DOWNLOAD_FOLDER):
        os.makedirs(settings.DOWNLOAD_FOLDER)

    app.register_blueprint(webhook_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5000, debug=True)