# ⚙️ Engineering Explorer

> Get insights into different engineering fields — explained your way.

Engineering Explorer is a Streamlit app powered by LangChain + Groq that generates AI-driven explanations for 30+ engineering disciplines. Pick a department, choose a style, and get a tailored breakdown instantly.

## Features

- 🔧 Covers 30+ engineering branches (CSE, ECE, Mechanical, Aerospace, and more)
- 🎨 Three explanation styles — Beginner-Friendly, Technical, or Funny
- 📏 Adjustable response length (short to detailed)
- ⚡ Fast inference via Groq API

## Setup

```bash
git clone https://github.com/Arijit-29/Engineering_explorer.git
cd engineering_explorer
pip install -r requirements.txt
```

Create a `.env` file with your API key:

```
GROQ_API_KEY=your_key_here
```

Then run:

```bash
streamlit run app.py
```

## Stack

- [Streamlit](https://streamlit.io/) — UI
- [LangChain](https://www.langchain.com/) — prompt management
- [Groq](https://groq.com/) — LLM inference
