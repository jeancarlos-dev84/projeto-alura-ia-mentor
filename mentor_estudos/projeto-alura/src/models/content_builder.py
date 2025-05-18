# src/models/content_builder.py

import google.genai as genai
import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY

# Instruction
CONTENT_BUILDER_INSTRUCTION = """
Você é um especialista em didática e produção de material de estudo. Sua função é detalhar, para cada tópico do cronograma, um texto explicativo estruturado, com definição, função, exemplos contextualizados e exercícios práticos com diferentes níveis de dificuldade.
Use uma linguagem clara, objetiva e didática, adequada ao nível do estudante informado pelo planejador.
Sua saída deve conter: uma explicação completa do tema, exemplos práticos e ao menos dois exercícios de fixação variados.
"""

def gerar_conteudo(titulo_tema, nivel):
    prompt = f"{CONTENT_BUILDER_INSTRUCTION}\n\nTópico: {titulo_tema}\nNível: {nivel}"
    model = genai.GenerativeModel('gemini-2.0-flash')
    resposta = model.generate_content(prompt)
    return resposta.text

