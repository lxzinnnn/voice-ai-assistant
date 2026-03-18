import os
from dotenv import load_dotenv

load_dotenv()

# Configurações de API
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY', 'sua-chave-aqui')

# Configurações de Voz
LANGUAGE = 'pt-BR'
SPEECH_RECOGNITION_TIMEOUT = 10
SPEECH_RECOGNITION_PHRASE_TIME_LIMIT = None

# Configurações de IA
AI_MODEL = 'gemini-pro'
AI_TEMPERATURE = 0.7

# Comandos especiais
COMMAND_START = ['iniciar', 'iniciar ia']
COMMAND_STOP = ['finalizar', 'parar']

# Status da IA
class AIStatus:
    IDLE = 'idle'
    LISTENING = 'listening'
    PROCESSING = 'processing'
    SPEAKING = 'speaking'
