from flask import Flask
from config import Config

# Create a Flask application instance
app = Flask(__name__, static_folder='static')

# Load configuration from Config class
app.config.from_object(Config)

# Import routes after app is created to avoid circular imports
from app import routes