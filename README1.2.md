# Oriki - Context-Aware Chatbot

A configurable chatbot interface that leverages the OpenAI GPT-4 API to adapt its communication style and responses based on predefined user identity and cultural context markers.

## Overview

Oriki is a web application built with Gradio that allows small businesses to deploy an AI-powered chatbot capable of mimicking their unique brand voice, slang, and cultural nuances, moving beyond generic, sterile automated responses.

## Features

- **Tone Customization:** Pre-set and customize the bot's communication style (e.g., poetic, direct, welcoming, informal).
- **Identity Phrases ("Orikis"):** Store key phrases that define the bot's personality and core identity.
- **Local Storage:** Save business profiles and their unique configurations locally using JSON or TinyDB.
- **Basic Analytics:** Monitor usage and interaction patterns.
- **Web Interface:** Simple, intuitive UI powered by Gradio.

## Technology Stack

- **Backend:** Python 3.8+
- **Web Framework:** Gradio
- **Generative AI:** OpenAI GPT-4 API
- **Storage:** JSON / TinyDB
- **Deployment Target:** Hugging Face Spaces, Render, Replit

## Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/MarcosIkutie/oriki-chatbot.git
    cd oriki-chatbot
    ```

2.  **Create a virtual environment and install dependencies:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Linux/MacOS
    # .venv\Scripts\activate  # Windows
    pip install -r requirements.txt
    ```

3.  **Set your OpenAI API key:**
    ```bash
    export OPENAI_API_KEY='your-openai-api-key-here'
    ```

4.  **Run the application:**
    ```bash
    python main.py
    ```

## Usage

1.  **Define Identity Phrases:** Input phrases that capture the essence of the business (e.g., "Love served in a pastry," "Only those from the hills understand our vibe").
2.  **Select a Tone:** Choose the desired communication style from the available options.
3.  **Interact:** Start a conversation through the web interface.
4.  **Customize:** Continuously adjust the bot's responses based on performance.

## Target Audience

- Neighborhood eateries and thrift stores.
- Tattoo studios and beauty salons.
- Independent artists, poets, and creators.
- Small businesses with a strong cultural identity.

## Roadmap

- Integration with WhatsApp Business API.
- Support for multiple languages (with a focus on African languages).
- Offline mobile version.
- Plugin system for extended functionality.
- Advanced analytical dashboard.

## License

This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).

**You are free to:**
- **Share:** Copy and redistribute the material in any medium or format.
- **Adapt:** Remix, transform, and build upon the material.

**Under the following terms:**
- **Attribution:** You must give appropriate credit, provide a link to the license, and indicate if changes were made.
- **NonCommercial:** You may not use the material for commercial purposes without explicit, formal authorization.
- **ShareAlike:** If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.

Any use, implementation, or monetization without formal authorization is subject to retroactive compensation.
