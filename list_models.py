
import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    print("Error: GROQ_API_KEY not set.")
    exit(1)

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

try:
    response = requests.get("https://api.groq.com/openai/v1/models", headers=headers)
    response.raise_for_status()
    models = response.json()
    
    with open("models_list.txt", "w") as f:
        for model in models['data']:
            f.write(f"{model['id']}\n")
    print("Models written to models_list.txt")
        
except Exception as e:
    print(f"Error fetching models: {e}")
