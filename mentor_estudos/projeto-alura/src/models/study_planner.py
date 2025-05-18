# src/models/study_planner.py

import google.genai as genai
import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY

# Instruction
STUDY_PLANNER_INSTRUCTION = """
Você é um planejador de estudos inteligente. Seu papel é criar um cronograma personalizado para o usuário com base nas informações fornecidas: tema de interesse, horas disponíveis por dia/semana, prazo para aprender.
Divida o conteúdo em sessões organizadas por dias/semanas, priorizando a progressão lógica dos tópicos e o equilíbrio da carga de estudo.
Sua saída deve ser um cronograma claro, indicando o que estudar em cada sessão e sugerindo a duração recomendada para cada bloco de estudo.
"""

def criar_cronograma(tema, horas_por_dia, prazo, nivel, preferencias):
    prompt = f"{STUDY_PLANNER_INSTRUCTION}\n\nTema: {tema}\nHoras por dia/semana: {horas_por_dia}\nPrazo: {prazo}\nNível: {nivel}\nPreferências: {preferencias}"
    model = genai.GenerativeModel('gemini-2.0-flash')
    resposta = model.generate_content(prompt)
    return resposta.text  