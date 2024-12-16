import openai
from openai import OpenAI
prompt = "What is the meaning of life?"
openai.api_key = 'skey'
print(10)
client = OpenAI(api_key=openai.api_key)
for i in client.models.list().data:
    print(i.id)
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "What is the meaning of life?"}],
    max_tokens=50  # Модель не сгенерирует больше 50 токенов в ответе
)

print(response.choices[0].text.strip())
