import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key or "YOUR_GEMINI_API_KEY" in api_key:
    print("❌ Error: API Key not set correctly in .env")
    exit(1)

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

try:
    print("Testing Gemini API connection...")
    response = model.generate_content("Hello, system check. Reply with 'Success' if you can read this.")
    print(f"Bot Response: {response.text.strip()}")
except Exception as e:
    print(f"❌ Gemini connection failed: {str(e)}")
