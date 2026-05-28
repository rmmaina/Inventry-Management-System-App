import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    sqlalchemy_track_modifications = False
    jwt_secret_key = os.getenv("JWT_SECRET_KEY")
    