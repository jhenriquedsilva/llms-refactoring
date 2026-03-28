from openai import OpenAI
from datetime import datetime

API_KEY = "YOUR_OPENAI_API_KEY"
MODEL = "gpt-4o"

client = OpenAI(api_key=API_KEY)

with open("prompt.txt", "r") as f:
    prompt = f.read().strip()

for i in range(1, 6):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    answer = response.choices[0].message.content
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(f"answer{i}.txt", "w") as f:
        f.write(f"{timestamp}\n\n{answer}\n")

    print(f"answer{i}.txt created")
