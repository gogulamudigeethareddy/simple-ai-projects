# AI Assistant Chatbot

This project is a simple AI-powered chatbot web app built with [Streamlit](https://streamlit.io/) and [LangChain](https://python.langchain.com/). It uses OpenAI's GPT-4o model to provide conversational AI capabilities.

## Features
- Chat with an AI assistant in your browser
- Remembers chat history during your session
- Powered by OpenAI's GPT-4o via LangChain
- Easy to run locally

## Requirements
- Python 3.8+
- An OpenAI API key ([get one here](https://platform.openai.com/account/api-keys))

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/simple-ai-projects.git
   cd simple-ai-projects
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   Or, if using [uv](https://github.com/astral-sh/uv):
   ```bash
   uv pip install -r requirements.txt
   ```
3. **Set up environment variables:**
   - Create a `.env` file in the project root with your OpenAI API key:
     ```env
     OPENAI_API_KEY=your-openai-api-key
     ```

## Usage
Run the chatbot app with Streamlit:
```bash
streamlit run chatbot.py
```
Open the URL in your browser to start chatting with the AI assistant.

## File Overview
- `chatbot.py` — Main Streamlit app
- `pyproject.toml` — Project metadata and dependencies
- `uv.lock` — Lockfile for reproducible installs (if using uv)
- `README.md` — This file


