# from openai import OpenAI
# from decouple import config

# client = OpenAI(api_key=config('OPENAI_API_KEY'))

def get_openai_response(conversation_history):
    try:
        # response = client.chat.completions.create(
        #     model="gpt-4",
        #     messages=conversation_history,
        #     temperature=0.7,
        #     max_tokens=1500
        # )
        # return response.choices[0].message.content
        pass
    except Exception as e:
        return f"Sorry, I encountered an error: {str(e)}"