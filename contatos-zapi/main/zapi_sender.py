 # zapi_sender.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()

ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")
ZAPI_INSTANCE = os.getenv("ZAPI_INSTANCE")

if not ZAPI_TOKEN or not ZAPI_INSTANCE:
    raise ValueError("ZAPI_TOKEN e ZAPI_INSTANCE devem estar configurados no .env")

def enviar_mensagem(telefone, nome):
    telefone = telefone.replace("+", "").replace(" ", "")
    mensagem = f"Olá {nome}, tudo bem com você?"

    # Print opcional para verificar a mensagem antes de enviar
    print(f"Mensagem que será enviada para {nome}: {mensagem}")

    url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE}/token/{ZAPI_TOKEN}/send-text"
    payload = {"phone": telefone, "message": mensagem}

    try:
        requests.post(url, json=payload)
    except requests.exceptions.RequestException:
        pass  # Mantém silencioso, apenas envia
