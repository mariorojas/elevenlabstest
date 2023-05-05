import os

import requests

# global values
XI_API_KEY = 'your-key'
CURRENT_DIR = os.getcwd()
FILE_PATH = f'{CURRENT_DIR}/example.mp3'
HISTORY_PATH = f'{CURRENT_DIR}/history.zip'

# retrieve default voice
resp = requests.get(
    url='https://api.elevenlabs.io/v1/voices',
    headers={'Accept': 'application/json'},
).json()

voice_id = resp['voices'][0]['voice_id']

# retrieve default voice settings
resp = requests.get(
    url='https://api.elevenlabs.io/v1/voices/settings/default',
    headers={'Accept': 'application/json'},
).json()

stability, similarity_boost = resp['stability'], resp['similarity_boost']

print(f'stability: {stability}...')
print(f'similarity_boost: {similarity_boost}...')

# process text to speech
resp = requests.post(
    url=f'https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/stream',
    headers={
        'Content-Type': 'application/json',
        'xi-api-key': XI_API_KEY
    },
    json={
        'text': 'Some very long text to be read by the voice',
        'voice_settings': {
            'stability': stability,
            'similarity_boost': similarity_boost
        }
    },
    stream=True
)

with open(FILE_PATH, 'wb') as file:
    for chunk in resp.iter_content(chunk_size=1024):
        if chunk:
            file.write(chunk)

print('audio file created successfully...')

# retrieve history, it should contained generated example
resp = requests.get(
    url='https://api.elevenlabs.io/v1/history',
    headers={
        'Accept': 'application/json',
        'xi-api-key': XI_API_KEY
    }
).json()

print(resp)

history = resp['history']

# download history
history_item_ids = [item['history_item_id'] for item in history]

resp = requests.post(
    url='https://api.elevenlabs.io/v1/history/download',
    headers={
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'xi-api-key': XI_API_KEY
    },
    json={
        'history_item_ids': history_item_ids
    }
)

with open(HISTORY_PATH, 'wb') as file:
    for chunk in resp.iter_content(chunk_size=1024):
        if chunk:
            file.write(chunk)

print('history downloaded successfully...')

# download history item
default_history_item = history_item_ids[0]

resp = requests.post(
    url='https://api.elevenlabs.io/v1/history/download',
    headers={
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'xi-api-key': XI_API_KEY
    },
    json={
        'history_item_ids': [
            default_history_item
        ]
    }
)

with open(f'{CURRENT_DIR}/{default_history_item}.mp3', 'wb') as file:
    for chunk in resp.iter_content(chunk_size=1024):
        if chunk:
            file.write(chunk)

print(f'history file {default_history_item} downloaded successfully...')
