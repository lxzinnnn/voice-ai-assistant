import google.generativeai as genai
from config import GOOGLE_API_KEY, AI_MODEL, AI_TEMPERATURE

class AIEngine:
    def __init__(self):
        """Inicializa o motor de IA"""
        genai.configure(api_key=GOOGLE_API_KEY)
        self.model = genai.GenerativeModel(AI_MODEL)
        self.conversation_history = []
    
    def is_command(self, text):
        """
        Verifica se o texto é um comando de controle
        Retorna: dict com info do comando ou None
        """
        from config import COMMAND_START, COMMAND_STOP
        
        for cmd in COMMAND_START:
            if cmd in text:
                return {'type': 'start', 'command': cmd}
        
        for cmd in COMMAND_STOP:
            if cmd in text:
                return {'type': 'stop', 'command': cmd}
        
        return None
    
    def analyze_and_respond(self, user_input):
        """
        Analisa a mensagem do usuário e gera resposta
        """
        try:
            # Adicionar ao histórico de conversação
            self.conversation_history.append({
                'role': 'user',
                'parts': [user_input]
            })
            
            # Criar prompt com contexto de conversa
            conversation_context = self._build_context()
            
            # Gerar resposta
            response = self.model.generate_content(
                conversation_context,
                generation_config=genai.types.GenerationConfig(
                    temperature=AI_TEMPERATURE,
                    max_output_tokens=200,
                )
            )
            
            ai_response = response.text
            
            # Adicionar ao histórico
            self.conversation_history.append({
                'role': 'model',
                'parts': [ai_response]
            })
            
            return ai_response
        
        except Exception as e:
            error_msg = f"Desculpe, ocorreu um erro: {str(e)}"
            print(f"❌ Erro na IA: {e}")
            return error_msg
    
    def _build_context(self):
        """Constrói o contexto da conversação"""
        context = "Você é um assistente de IA amigável e útil. Responda de forma concisa e natural. "
        context += "Você pode ajudar com perguntas, fornecer informações, ou simplesmente conversar. "
        
        # Adicionar histórico recente (últimas 5 trocas)
        for msg in self.conversation_history[-10:]:
            role = "Usuário" if msg['role'] == 'user' else "Você"
            context += f"\n{role}: {msg['parts'][0]}"
        
        return context
    
    def reset_conversation(self):
        """Reseta o histórico de conversação"""
        self.conversation_history = []
