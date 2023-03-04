import openai
import requests
from decouple import config


# Retrieve Enviornment Variables
openai.organization = config("OPEN_AI_ORG")
openai.api_key = config("OPEN_AI_KEY")


# Open AI - Whisper
# Convert audio to text
def convert_audio_to_text(audio_file):
  try:
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    message_text = transcript["text"]
    return message_text
  except Exception as e:
    return

# Open AI - Chat GPT
# Convert audio to text
def get_chat_response(message_input):
  try:
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": " \
             You are teaching me Spanish. My name is Shaun. \
             Give me positive reinforcement and keep the conversation going. \
             You can include the occasional humour\
             "},
            {"role": "user", "content": "How do I ask where the train station is?"},
            {"role": "assistant", "content": "You can ask ¿Dónde está la estación de tren? which means Where is the train station?."},
            {"role": "user", "content": message_input}
        ]
    )
    message_text = response["choices"][0]["message"]["content"]
    return message_text
  except Exception as e:
    return
