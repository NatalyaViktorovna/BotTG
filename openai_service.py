import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

def translate_text(text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Ты переводчик с русского на английский."},
                {"role": "user", "content": text}
            ],
            max_tokens=1000,
            temperature=0.3
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"Ошибка перевода: {e}"