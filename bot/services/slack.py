from slack_bolt import App
from bot.models import Conversation
from bot.services.ai import get_ai_response
from backend.constants import SLACK_BOT_TOKEN, SLACK_SIGNING_SECRET

app = App(
    token = SLACK_BOT_TOKEN,
    signing_secret = SLACK_SIGNING_SECRET,
    token_verification_enabled=False,
)

@app.event("app_mention")
def handle_app_mentions(event, say):
    channel_id = event["channel"]
    user_id = event["user"]
    message = event["text"]
    previous_conversations = Conversation.objects.filter(
        channel_id=channel_id
    ).order_by('-timestamp')[:5]
    response = get_ai_response(previous_conversations)
    Conversation.objects.create(
        channel_id=channel_id,
        user_id=user_id,
        message=message,
        response=response
    )
    say(text=response, thread_ts=event["ts"])
