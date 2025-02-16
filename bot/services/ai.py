import requests
from backend.constants import (OPEN_ROUTER_API_KEY, BASE_URL,)


def get_ai_response(conversation_history) -> str:
    data = {
        'model': 'deepseek/deepseek-r1:free',
        'messages': [{
            'role': 'user',
            'content': f'Draft a response to the message and I have attached the following message history context:\n{conversation_history}\n. Write a response that is concise and to the point. Do not add any extra information. If the message is not related to the context, respond with "I am sorry, I do not understand the message". Do not add any extra information. If the message is not related to the context, respond with "I am sorry, I do not understand the message". Do not add any extra information. If the message is not related to the context, respond with "I am sorry, I do not understand the message".',
        }],
    }
    try:
        headers = {
            'Authorization': f'Bearer {OPEN_ROUTER_API_KEY}',
            'Content-Type': 'application/json',
        }
        response = requests.post(BASE_URL, json=data, headers=headers)
        response.raise_for_status()
        response_data = response.json()
        return response_data['choices'][0]['message']['content']
    except Exception as e:
        print(e)
        return f"Sorry, I encountered an error. Please try again later."
