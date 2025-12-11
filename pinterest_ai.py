import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

PROMPT_TEMPLATE = """
Ты — генератор Pinterest-постов.
Входной текст: первая строка — TITLE товара, дальше — DESCRIPTION.
Нужно выдать:
• Pinterest Title
• Pinterest Description
• 10–20 хэштегов
• Alt-text

Дай ответ в удобном формате.
Текст:
{{INPUT}}
"""

def generate_pinterest_post(text: str) -> str:
    prompt = PROMPT_TEMPLATE.replace("{{INPUT}}", text)

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    # В новой версии OpenAI так достаётся текст ответа
    return response.choices[0].message.content