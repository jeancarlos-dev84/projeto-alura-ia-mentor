# src/agents/flash_master.py

import google.genai as genai
import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY

# Instruction
FLASHMASTER_INSTRUCTION = """
Você é um gerador de flashcards didáticos para revisão rápida. Sua tarefa é analisar o conteúdo produzido pelo Criador de Conteúdo e identificar os principais conceitos do tópico.
Para cada tópico, produza 5 flashcards no formato de pergunta e resposta, alternando entre questões de completar frases, verdadeiro ou falso, e múltipla escolha, sempre garantindo clareza e foco nos pontos essenciais.
Organize os flashcards em ordem lógica de aprendizado e evite repetições.
"""

def gerar_flashcards(conteudo):
    prompt = f"{FLASHMASTER_INSTRUCTION}\n\nConteúdo:\n{conteudo}\n\nRetorne os flashcards no formato:\n1. Pergunta\n   Resposta\n..."
    model = genai.GenerativeModel('gemini-2.0-flash')
    resposta = model.generate_content(prompt)
    return resposta.text

