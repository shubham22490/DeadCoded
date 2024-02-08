import requests

CHUNK_SIZE = 1024
key = "01ac859eeb04fadac37ac177c1c4dd6e"


def generate_audio(sentence: str, voice_type: str, api_key: str) -> str:
    url = ""
    if voice_type == 'female':
        url = "https://api.elevenlabs.io/v1/text-to-speech/AZnzlk1XvdvUeBnXmlld"
    elif voice_type == 'male':
        url = "https://api.elevenlabs.io/v1/text-to-speech/29vD33N1CtxCmqQRPOHJ"
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": api_key
    }
    data = {
        "text": sentence,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }
    response = requests.post(url, json=data, headers=headers)
    with open('output.mp3', 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)
    return 'output.mp3'


generate_audio("यह काम कर रहा है", "male", key)
