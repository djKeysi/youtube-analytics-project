from googleapiclient.discovery import build
import os
import json

# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('YouTube_API')

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)

channel_id = 'UCwHL6WHUarjGfUM_586me8w'  # HighLoad Channel
channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

def printj(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

printj(channel)