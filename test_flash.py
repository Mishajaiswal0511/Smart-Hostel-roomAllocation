import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-flash-latest')

try:
    print("Testing gemini-flash-latest connection...")
    response = model.generate_content("Hello, system check. Are you active?")
    print(f"Bot Response: {response.text.strip()}")
except Exception as e:
    print(f"Status: {e}")
