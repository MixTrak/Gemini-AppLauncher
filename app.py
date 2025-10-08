import google.generativeai as genai
from dotenv import load_dotenv
import subprocess
import re
import os

# Load environment variables from .env.local
load_dotenv(dotenv_path='.env.local')

# Configure the API key
API_KEY = os.getenv("API_KEY")
genai.configure(api_key=API_KEY)

# Mac application mappings
APPS = {
    'vscode': 'Visual Studio Code', 'code': 'Visual Studio Code',
    'chrome': 'Google Chrome', 'operagx': 'Opera GX', 'opera': 'Opera',
    'finder': 'Finder', 'safari': 'Safari', 'terminal': 'Terminal',
    'notes': 'Notes', 'messages': 'Messages', 'mail': 'Mail',
    'music': 'Music', 'spotify': 'Spotify',
}

def open_app(name):
    """Open macOS app"""
    app = APPS.get(name.lower())
    if app:
        try:
            subprocess.Popen(['open', '-a', app], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return f"✓ Opened {app}"
        except:
            return f"✗ Could not open {app}"
    return f"✗ Unknown app: {name}"

def get_models():
    """Get available models"""
    try:
        return [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    except:
        return []

def switch_model(models, current):
    """Switch model"""
    print("\n" + "=" * 50)
    for i, m in enumerate(models, 1):
        print(f"{i:2}. {m}{' <- CURRENT' if m == current else ''}")
    print("=" * 50)
    
    while True:
        choice = input("\nModel Number (or 'c' to cancel): ").strip()
        if choice.lower() == 'c':
            return current
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(models):
                print(f"✓ Switched to: {models[idx]}")
                return models[idx]
        except:
            pass

def main():
    print("-" * 50)
    print("Gemini Chatbot")
    print("-" * 50)
    
    models = get_models()
    if not models:
         print("No models available.")
         return
    
    # Use fastest model by default
    model_name = next((m for m in models if 'flash' in m.lower()), models[0])
    print("-" * 50)
    print(f"Model: {model_name}")
    print("Command: 'open [app]' | 'switch'")
    print(API_KEY)
    print("-" * 50)
    
    model = genai.GenerativeModel(model_name)
    chat = model.start_chat(history=[])
    
    while True:
        try:
            inp = input("\nYou: ").strip()
            if not inp:
                continue
            
            # Check for open command
            match = re.match(r'open\s+(\w+)', inp.lower())
            if match:
                print(f"\n{open_app(match.group(1))}")
                continue
            
            # Check for switch command
            if inp.lower() in ['switch', 'model', 'models']:
                new = switch_model(models, model_name)
                if new != model_name:
                    model_name = new
                    model = genai.GenerativeModel(model_name)
                    chat = model.start_chat(history=[])
                continue
            
            # Send to AI
            response = chat.send_message(inp)
            print(f"\nAI: {response.text}")
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {e}")

if __name__ == "__main__":
    main()