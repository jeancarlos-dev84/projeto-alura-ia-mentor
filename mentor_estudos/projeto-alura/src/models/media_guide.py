# src/agents/media_guide.py

import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

# Instruction
MEDIA_GUIDE_INSTRUCTION = """
Você é um curador de recursos multimídia focado em reforçar o aprendizado do estudante. Sua tarefa é pesquisar vídeos no YouTube que complementem o conteúdo do tópico em estudo.
Para cada tópico, selecione exatamente 2 vídeos relevantes, priorizando qualidade didática, objetividade e reputação do criador.
Para cada vídeo sugerido, forneça o título, o link e uma breve descrição do que o estudante encontrará no vídeo.
"""

def buscar_videos_youtube(tema, max_results=2):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    search_response = youtube.search().list(
        q=tema,
        part='snippet',
        maxResults=max_results,
        type='video'
    ).execute()
    resultados = []
    for item in search_response.get('items', []):
        resultados.append({
            'titulo': item['snippet']['title'],
            'url': f"https://www.youtube.com/watch?v={item['id']['videoId']}",
            'descricao': item['snippet']['description']
        })
    return resultados

