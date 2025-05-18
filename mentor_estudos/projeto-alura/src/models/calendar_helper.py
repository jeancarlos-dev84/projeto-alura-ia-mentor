# src/models/calendar_helper.py

from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

def adicionar_evento_calendar(session, evento):
    """
    Adiciona um evento ao Google Calendar do usuário autenticado via OAuth.
    - session: objeto de sessão Flask com as credenciais do usuário.
    - evento: dicionário com 'titulo', 'descricao', 'inicio', 'fim' (datas no formato ISO 8601).
    """
    creds = Credentials(**session['credentials'])
    service = build('calendar', 'v3', credentials=creds)
    evento_google = {
        'summary': evento['titulo'],
        'description': evento.get('descricao', ''),
        'start': {
            'dateTime': evento['inicio'],
            'timeZone': 'America/Sao_Paulo',
        },
        'end': {
            'dateTime': evento['fim'],
            'timeZone': 'America/Sao_Paulo',
        },
    }
    event = service.events().insert(calendarId='primary', body=evento_google).execute()
    return event['id']