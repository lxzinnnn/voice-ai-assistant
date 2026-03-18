# 🎤 Assistente de IA com Detecção de Voz

Um assistente de IA inteligente que conversa com você usando **reconhecimento de voz** e **síntese de voz** em português.

## ✨ Características

- 🎤 **Detecção de Voz**: Reconhecimento excelente para frases curtas e longas
- 🤖 **Resposta com IA**: Usa Google Gemini para respostas inteligentes
- 🔊 **Síntese de Voz**: Responde com voz natural em português
- 🔄 **Conversação Contínua**: Loop que se mantém ativo até você falar "finalizar"
- ⚡ **Início/Fim Espontâneo**: Comande com "iniciar" e "finalizar"

## 🚀 Como Usar

### 1. Instalação

```bash
# Clone o repositório
git clone https://github.com/lxzinnnn/voice-ai-assistant
cd voice-ai-assistant

# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

### 2. Configuração da API

1. Obtenha uma chave de API do Google Gemini em: https://makersuite.google.com/app/apikey
2. Crie um arquivo `.env` na pasta raiz:
```
GOOGLE_API_KEY=sua-chave-aqui
```

### 3. Execute o Programa

```bash
python main.py
```

## 💬 Como Usar

1. **Inicie a IA**: Diga **"iniciar"**
2. **Converse**: Faça perguntas ou converse normalmente
3. **Finalize**: Diga **"finalizar"** para parar
4. **Reinicie**: Diga **"iniciar"** novamente para continuar

### Exemplos de Uso:

```
Você: "Iniciar"
IA: [Começa a ouvir]

Você: "Qual é a capital da França?"
IA: "A capital da França é Paris..."

Você: "Me conte uma piada"
IA: "Claro! Por que o livro de matemática se suicidou?..."

Você: "Finalizar"
IA: [Para de ouvir]
```

## 🎯 Próximos Passos

- [ ] Adicionar comandos para abrir aplicativos
- [ ] Integrar controle de música
- [ ] Controle de luzes inteligentes
- [ ] Desligamento do PC
- [ ] Controle de redes sociais
- [ ] Agendamento de tarefas

## 📋 Requisitos

- Python 3.8+
- Microfone funcional
- Conexão com internet (para API Google)
- Windows/Linux/Mac

## 🔧 Configurações Personalizáveis

Em `config.py` você pode ajustar:

- **LANGUAGE**: Idioma (pt-BR, en-US, etc)
- **AI_TEMPERATURE**: Criatividade da IA (0-1)
- **SPEECH_RECOGNITION_TIMEOUT**: Tempo máximo de escuta
- Velocidade e volume da voz

## ⚠️ Troubleshooting

### "Erro ao instalar pyaudio"

**Windows:**
```bash
pip install pipwin
pipwin install pyaudio
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install portaudio19-dev
pip install pyaudio
```

**Mac:**
```bash
brew install portaudio
pip install pyaudio
```

### "Erro de conexão com API"

Verifique se sua chave de API está correta no arquivo `.env`

## 📞 Suporte

Para dúvidas ou problemas, abra uma issue no GitHub.

## 📄 Licença

MIT License - veja LICENSE para mais detalhes.
