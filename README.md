# Test script for ElevenLabs TTS (Text To Speech)

**INSTALLATION COMMANDS**

```
git clone https://github.com/mariorojas/elevenlabstest.git
cd elevenlabstest/
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

Make sure to get your [ElevenLabs API key](https://docs.elevenlabs.io/authentication/01-xi-api-key) and set it in **main.py**

```
XI_API_KEY = 'your-key'
```

To create an audio file, run the following:

```
python main.py
# output: stability...
```