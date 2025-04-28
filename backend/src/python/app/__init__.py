from flask import Flask
from config import DevelopmentConfig
from app.models.model import OllamaClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config.from_object(DevelopmentConfig)
ollamaClient = OllamaClient()

from app import routes