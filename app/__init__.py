from flask import Flask
from flask_cors import CORS
import os

def create_app():
    app = Flask(__name__)
    CORS(app) # Allow frontend to communicate with backend
    
    # Ensure upload and session directories exist
    os.makedirs('uploads', exist_ok=True)
    os.makedirs('sessions', exist_ok=True)

    # Register blueprints/routes
    from app.routes import main
    app.register_blueprint(main)

    return app