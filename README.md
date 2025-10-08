# Gemini AI Chatbot

Gemini AI is a macOS-focused chatbot built with **Google AI Studio** that allows you to:

- Switch between AI models dynamically.
- Open configurable apps directly from the terminal.
- Chat interactively with AI using the selected model.

---

## Features

- **Switch Models:** Use multiple generative AI models and change them on-the-fly.  
- **Open Apps:** Launch macOS applications like VSCode, Chrome, Finder, Spotify, and more.  
- **Configurable Apps:** Easily add or remove apps in the `APPS` dictionary (line ~15 in the code).  
- **Secure API Key Management:** Store your Google AI Studio API key in `.env.local`.

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/gemini-ai.git
cd gemini-ai
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

*Requirements include `google-generativeai` and `python-dotenv`.*

### 3. Create `.env.local`

Store your Google AI Studio API key:

```bash
echo "API_KEY=your_google_ai_studio_api_key" > .env.local
```

> The key will be automatically loaded by the script. Keep `.env.local` in `.gitignore` to protect it.

---

## Usage

### 1. Run the Chatbot

```bash
python main.py
```

You will see:

```
Gemini Chatbot
Model: gemini-v2
Command: 'open [app]' | 'switch'
```

---

### 2. Commands

#### Open Apps

```bash
open <app_name>
```

**Examples:**

```bash
open vscode
open chrome
open spotify
```

If the app is not recognized, an error message will appear.

#### Switch Models

```bash
switch
```

The script lists available models. Enter the number of the model you want to use, or `c` to cancel:

```
1. gemini-v1
2. gemini-v2 <- CURRENT
3. gemini-flash
```

#### Chat

Type any message to chat with the AI:

```
You: Hello Gemini!
AI: Hi! How can I help you today?
```

---

## Configuration

* **Apps:** Modify the `APPS` dictionary in the code to add or remove macOS applications.
* **Default Model:** The script selects a “flash” model by default if available; otherwise, it uses the first available model.

---

## Contribution

1. Fork the repository
2. Create a branch: `git checkout -b feature/new-feature`
3. Make your changes
4. Commit: `git commit -m "Add new feature"`
5. Push: `git push origin feature/new-feature`
6. Open a Pull Request

---
