import requests

INSTANCE_ID = '3E5A8499468820B08F561EB6C5359192'
ZAPI_TOKEN = 'BA45EBCCD3A590778050C52F'
CLIENT_TOKEN = 'F0e8d3729fc834b1fada16133c9569423S'

# Contatos
DIEGO = '5522997168009'
LIAM = '558897307934'
MARIA = '5522997269204'

headers = {
    'Client-Token': CLIENT_TOKEN,
    'Content-Type': 'application/json'
}

def send_message(number, text):
    payload = {
        'phone': number,
        'message': text,
    }
    response = requests.post(
        url=f'https://api.z-api.io/instances/{INSTANCE_ID}/token/{ZAPI_TOKEN}/send-text',
        json=payload,
        headers=headers,
    )
    return response.json()

# Teste com os contatos
payload = {
    'phone': MARIA,  # Maria: 5522997269204
    'message': 'Olá Maria_5522997269204, Tudo bem com você?',
}

response = requests.post(
    url=f'https://api.z-api.io/instances/{INSTANCE_ID}/token/{ZAPI_TOKEN}/send-text',
    json=payload,
    headers=headers,
)
print(response.json())
