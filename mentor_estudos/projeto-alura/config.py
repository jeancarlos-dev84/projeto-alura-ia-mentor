import os
from dotenv import load_dotenv

# Caminho absoluto para o arquivo .env
dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')

# Carregar as variáveis do arquivo .env
load_dotenv(dotenv_path)

# Carregar as variáveis
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")