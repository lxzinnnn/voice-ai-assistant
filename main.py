import time
from config import AIStatus, COMMAND_START, COMMAND_STOP
from voice_handler import VoiceHandler
from ai_engine import AIEngine

class VoiceAIAssistant:
    def __init__(self):
        """Inicializa o assistente de voz"""
        print("🚀 Iniciando Assistente de IA com Detecção de Voz...")
        self.voice = VoiceHandler()
        self.ai = AIEngine()
        self.status = AIStatus.IDLE
        self.is_running = False
    
    def check_command(self, text):
        """Verifica se é um comando de controle"""
        if not text:
            return None
        
        # Verificar comando de iniciar
        for cmd in COMMAND_START:
            if cmd in text:
                return 'start'
        
        # Verificar comando de finalizar
        for cmd in COMMAND_STOP:
            if cmd in text:
                return 'stop'
        
        return None
    
    def start(self):
        """Inicia o loop de conversação"""
        print("\n" + "="*50)
        print("✅ IA INICIADA - Diga 'finalizar' para parar")
        print("="*50 + "\n")
        
        self.is_running = True
        self.status = AIStatus.LISTENING
        self.ai.reset_conversation()
        
        while self.is_running:
            try:
                # Ouvir entrada do usuário
                user_input = self.voice.listen()
                
                if user_input is None:
                    continue
                
                # Verificar se é um comando
                command = self.check_command(user_input)
                
                if command == 'stop':
                    self.stop()
                    break
                
                # Se não for comando, processar como mensagem normal
                if command is None:
                    self.status = AIStatus.PROCESSING
                    
                    # Gerar resposta da IA
                    response = self.ai.analyze_and_respond(user_input)
                    
                    self.status = AIStatus.SPEAKING
                    
                    # Falar a resposta
                    self.voice.speak(response)
                    
                    self.status = AIStatus.LISTENING
                    
                    # Pequena pausa antes de ouvir novamente
                    time.sleep(1)
            
            except KeyboardInterrupt:
                print("\n⚠️ Interrompido pelo usuário")
                self.stop()
                break
            except Exception as e:
                print(f"❌ Erro na conversação: {e}")
                continue
    
    def stop(self):
        """Para o loop de conversação"""
        print("\n" + "="*50)
        print("🛑 IA FINALIZADA")
        print("="*50)
        print("💡 Para iniciar novamente, diga 'iniciar'\n")
        
        self.is_running = False
        self.status = AIStatus.IDLE
    
    def run_main_loop(self):
        """Loop principal - aguarda comando de iniciar"""
        print("\n" + "="*50)
        print("🎤 ASSISTENTE DE IA COM DETECÇÃO DE VOZ")
        print("="*50)
        print("💬 Diga 'INICIAR' para começar")
        print("="*50 + "\n")
        
        while True:
            try:
                print("Aguardando comando de iniciar...")
                user_input = self.voice.listen()
                
                if user_input is None:
                    continue
                
                # Verificar se é comando de iniciar
                command = self.check_command(user_input)
                
                if command == 'start':
                    self.start()
                    # Após finalizar, volta ao loop principal
                    continue
                else:
                    print("⚠️ Para iniciar, diga 'INICIAR'\n")
            
            except KeyboardInterrupt:
                print("\n👋 Encerrando assistente...")
                break
            except Exception as e:
                print(f"❌ Erro: {e}")
                continue

if __name__ == "__main__":
    assistant = VoiceAIAssistant()
    assistant.run_main_loop()
