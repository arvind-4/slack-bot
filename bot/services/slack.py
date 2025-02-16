from slack_bolt import App
from bot.models import Conversation
from slack_bolt.adapter.django import SlackRequestHandler
from backend.constants import (SLACK_BOT_TOKEN, SLACK_SIGNING_SECRET,)

app = App(
    token = SLACK_BOT_TOKEN,
    signing_secret = SLACK_SIGNING_SECRET,
)

handler = SlackRequestHandler(app)

@app.event("app_mention")
def handle_mention(event, say):
    print("Event:", event)
    print("Say:", say)
    channel_id = event["channel"]
    user_id = event["user"]
    message = event["text"]
    print("Channel ID:", channel_id)
    print("User ID:", user_id)
    print("Message:", message)
    
    # previous_conversations = Conversation.objects.filter(
    #     channel_id=channel_id
    # ).order_by('-timestamp')[:5]

    # conversation_history = []
    # for conv in reversed(previous_conversations):
    #     conversation_history.append({"role": "user", "content": conv.message})
    #     conversation_history.append({"role": "assistant", "content": conv.response})
    
    # conversation_history.append({"role": "user", "content": message})
    
    # # Get response from OpenAI
    # # response = get_openai_response(conversation_history)
    
    # # Save conversation
    # Conversation.objects.create(
    #     channel_id=channel_id,
    #     user_id=user_id,
    #     message=message,
    #     response=""
    # )
    
    # Reply in thread
    say(text="Hello", thread_ts=event["ts"])