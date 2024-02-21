#sk-NxyHHejYAb9f0dVS12qZbHe8LitQZyjb - мой личный API
from openai import OpenAI

client = OpenAI(
    api_key="sk-NxyHHejYAb9f0dVS12qZbHe8LitQZyjb",
    base_url="https://api.proxyapi.ru/openai/v1",
)

messages = []

while True:
    user_input = input("You: ")
    
    messages.append({"role": "user", "content": user_input})

    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages
    )
    
    ai_response = chat_completion.choices[0].message.content  
    print("AI:", ai_response)
    
    messages.append({"role": "system", "content": ai_response})

    if user_input.lower() == 'quit':
        print("Exiting the chat...")
        break