import google.generativeai as genai
from dotenv import load_dotenv
import os
from typing import Final

def generate_menfess():
    try:
        load_dotenv()
        KEY: Final[str] = os.getenv('API_KEY')
        genai.configure(api_key=KEY)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content("create a random funny text for menfess as like a 19 years old teenager. make it more of a funny joke than a personal experience")
        result = response.text
        return result
    except:
        return "error"

def reply_with_AI(message):
    try:
        load_dotenv()
        KEY: Final[str] = os.getenv('API_KEY')
        genai.configure(api_key=KEY)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(f"pretend you are his/her friend. reply his/her menfess message '{message}'. try to be as silly and funny as possible")
        result = response.text
        return result
    except:
        return "error"
    
if __name__ == "__main__":
    message = ''
    print(generate_menfess(message))