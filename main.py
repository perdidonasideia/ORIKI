import gradio as gr
import openai
import json
from prompts import gerar_prompt_base

# Carregar configurações (oriki + tom) - versão simples
def carregar_config():
    try:
        with open("config.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "orikis": [],
            "tom": "neutro"
        }

# Salvar configurações
def salvar_config(orikis, tom):
    config = {"orikis": orikis, "tom": tom}
    with open("config.json", "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)

# Função de chat
def responder(mensagem, historia, orikis, tom):
    prompt_sistema = gerar_prompt_base(orikis, tom)
    mensagens = [{"role": "system", "content": prompt_sistema}]
    for user, bot in historia:
        mensagens.append({"role": "user", "content": user})
        mensagens.append({"role": "assistant", "content": bot})
    mensagens.append({"role": "user", "content": mensagem})

    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-4",
            messages=mensagens,
            temperature=0.9,
            max_tokens=300
        )
        texto_resposta = resposta.choices[0].message["content"]
    except Exception as e:
        texto_resposta = f"(Erro ao chamar API: {e})"

    historia.append((mensagem, texto_resposta))
    return historia, historia

# Interface do formulário de personalização
def salvar_form(oriki1, oriki2, oriki3, tom):
    orikis = [oriki1, oriki2, oriki3]
    salvar_config(orikis, tom)
    return "Configurações salvas com sucesso!"

# Carregar config inicial
cfg = carregar_config()

# Gradio Blocks UI
with gr.Blocks() as demo:
    gr.Markdown("# 🧠 Oriki Chatbot")
    with gr.Tab("Chat"):
        chatbot = gr.Chatbot()
        msg = gr.Textbox(label="Sua mensagem")
        state = gr.State([])

        oriki_inputs = [gr.Textbox(label=f"Oriki {i+1}", value=cfg['orikis'][i] if i < len(cfg['orikis']) else "") for i in range(3)]
        tom_dropdown = gr.Dropdown(choices=["neutro", "poético", "direto", "engraçado", "periférico"], value=cfg["tom"], label="Tom do Oriki")

        msg.submit(responder, [msg, state, *oriki_inputs, tom_dropdown], [chatbot, state])

    with gr.Tab("Configuração"):
        gr.Markdown("### Personalize seu Oriki")
        salvar_btn = gr.Button("Salvar Configurações")
        output = gr.Textbox(label="Status")
        salvar_btn.click(salvar_form, [*oriki_inputs, tom_dropdown], output)

demo.launch()
