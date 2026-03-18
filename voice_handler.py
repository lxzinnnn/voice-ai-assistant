import speech_recognition as sr
import pyttsx3
from config import LANGUAGE, SPEECH_RECOGNITION_TIMEOUT

class VoiceHandler:
    def __init__(self):
        """Inicializa os componentes de voz"""
        # Reconhecimento de voz
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 4000
        self.recognizer.dynamic_energy_threshold = True
        
        # Síntese de voz
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # Velocidade
        self.engine.setProperty('volume', 0.9)  # Volume
        
        # Configurar idioma português
        voices = self.engine.getProperty('voices')
        for voice in voices:
            if 'pt' in voice.languages or 'Portuguese' in voice.name:
                self.engine.setProperty('voice', voice.id)
                break
    
    def listen(self):
        """
        Ouve o áudio do microfone e converte em texto
        Retorna: str ou None
        """
        try:
            with sr.Microphone() as source:
                print("🎤 Ouvindo...")
                # Ajustar ruído ambiente
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                
                # Capturar áudio
                audio = self.recognizer.listen(
                    source,
                    timeout=SPEECH_RECOGNITION_TIMEOUT,
                    phrase_time_limit=None
                )
            
            # Reconhecer fala usando Google Speech Recognition
            print("🔄 Processando áudio...")
            text = self.recognizer.recognize_google(audio, language=LANGUAGE)
            print(f"📝 Você disse: {text}")
            return text.lower()
        
        except sr.UnknownValueError:
            print("❌ Não consegui entender. Tente novamente.")
            return None
        except sr.RequestError as e:
            print(f"⚠️ Erro de conexão: {e}")
            return None
        except Exception as e:
            print(f"❌ Erro ao ouvir: {e}")
            return None
    
    def speak(self, text):
        """
        Converte texto em fala e reproduz
        """
        try:
            print(f"🤖 IA: {text}")
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            print(f"❌ Erro ao falar: {e}")
