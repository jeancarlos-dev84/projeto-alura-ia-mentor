from flask import Flask, render_template, request, flash
from dotenv import load_dotenv
import os

# === IMPORTANDO OS AGENTES DE ESTUDO ===
from models.study_planner import criar_cronograma
from models.content_builder import gerar_conteudo
from models.flash_master import gerar_flashcards
from models.media_guide import buscar_videos_youtube

# Carregar as variáveis do arquivo .env
load_dotenv()
DEMO_MODE = os.getenv("DEMO_MODE", "False") == "True"

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY") or "minha-chave-supersecreta-123"

@app.route('/')
def index():
    # Renderiza a interface principal (use 'home.html' ou 'estudar.html' para conteúdo completo)
    return render_template('home.html', demo_mode=DEMO_MODE)

# ============= ROTA PARA INICIAR UM ESTUDO =============
@app.route('/estudar', methods=['GET', 'POST'])
def estudar():
    if request.method == 'POST':
        tema = request.form.get('tema', '')
        prazo = request.form.get('prazo', '')
        disponibilidade = request.form.get('disponibilidade', '')
        nivel = request.form.get('nivel', '')
        preferencias = request.form.get('preferencias', '')

        if DEMO_MODE:
            # --- SIMULAÇÃO DOS AGENTES ---
            cronograma = [
                {
                    "tema": tema,
                    "descricao": f"Estudo do tema '{tema}' conforme suas preferências.",
                    "inicio": "2025-05-20T14:00:00-03:00",
                    "fim": "2025-05-20T16:00:00-03:00"
                }
            ]
            # NOVA LINHA de conteúdo simulado
            conteudo = f"O tema selecionado foi: {tema}. Aqui está um resumo: {tema} é um assunto importante que envolve vários conceitos fundamentais. [Simulação de conteúdo gerado pelo agente de IA]."
            flashcards = [
                {"pergunta": "O que é mitocôndria?", "resposta": "Organela responsável pela respiração celular."},
                {"pergunta": "Qual a função do núcleo?", "resposta": "Armazenar o material genético."},
                {"pergunta": "Exemplo de célula animal?", "resposta": "Célula muscular."}
            ]
            videos = [
                {"titulo": "Introdução ao tema", "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ", "descricao": "Vídeo introdutório"},
                {"titulo": "Aprofundamento", "url": "https://www.youtube.com/watch?v=ZZ5LpwO-An4", "descricao": "Conteúdo avançado"}
            ]
            planejamento_resumo = f"Estude {tema} durante {disponibilidade} ao longo de {prazo}."
            resumo_salvo = True  # Simula o salvamento
            flash("Modo demonstração: as integrações com Google e YouTube são simuladas.", "info")
        else:
            # --- FLUXO REAL DOS AGENTES E CALENDAR ---
            cronograma = criar_cronograma(tema, disponibilidade, prazo, nivel, preferencias)
            conteudo = gerar_conteudo(tema, nivel)
            flashcards = gerar_flashcards(conteudo)
            videos = buscar_videos_youtube(tema)
            planejamento_resumo = "Resumo gerado pelo agente."
            resumo_salvo = True  # Aqui você pode chamar adicionar_evento_calendar()

        return render_template(
            'estudar.html',
            cronograma=cronograma,
            conteudo=conteudo,
            flashcards=flashcards,
            videos=videos,
            planejamento_resumo=planejamento_resumo,
            resumo_salvo=resumo_salvo,
            demo_mode=DEMO_MODE
        )
    return render_template('estudar.html', demo_mode=DEMO_MODE)

if __name__ == '__main__':
    app.run(debug=True)

    