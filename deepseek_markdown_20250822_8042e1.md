# 🤖 Oriki - Chatbot com Alma e Contexto

> Um chatbot inteligente que adapta sua linguagem ao contexto, intenção e identidade cultural do usuário, inspirado na tradição Iorubá dos orikis.

[![Licença CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
[![OpenAI GPT-4](https://img.shields.io/badge/OpenAI-GPT--4-green.svg)](https://openai.com)

## 🌟 Visão Geral

Oriki é uma solução de atendimento automatizado para pequenos negócios que desejam manter sua autenticidade cultural e linguística nas interações digitais. Diferente de chatbots genéricos, o Oriki adapta sua fala ao contexto específico de cada negócio, preservando gingas, sotaques e identidades únicas.

## ✨ Funcionalidades

- **Personalização de Linguagem**: Adapta o tom de voz (poético, direto, acolhedor, periférico)
- **Banco de Orikis**: Armazena frases identitárias que definem a personalidade do bot
- **Interface Intuitiva**: Web app construído com Gradio para fácil interação
- **Integração com GPT-4**: Utiliza modelos avançados de linguagem natural
- **Armazenamento Local**: Perfis de negócios salvos em JSON ou TinyDB
- **Analytics Básicos**: Monitoramento de uso e interações

## 🛠️ Tecnologias

- **Backend**: Python 3.8+
- **Framework Web**: Gradio
- **IA Generativa**: OpenAI GPT-4 API
- **Armazenamento**: JSON local / TinyDB
- **Deploy**: Hugging Face Spaces / Render / Replit (futuro)

## 📦 Instalação

```bash
# Clone o repositório
git clone https://github.com/MarcosIkutie/oriki-chatbot.git

# Acesse o diretório
cd oriki-chatbot

# Instale as dependências
pip install -r requirements.txt

# Configure sua API key da OpenAI
export OPENAI_API_KEY='sua-chave-aqui'

# Execute a aplicação
python main.py