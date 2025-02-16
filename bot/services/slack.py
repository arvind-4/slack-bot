import logging
from slack_bolt import App
from bot.services.ai import get_ai_response
from backend.constants import SLACK_BOT_TOKEN, SLACK_SIGNING_SECRET

logger = logging.getLogger(__name__)

app = App(
    token = SLACK_BOT_TOKEN,
    signing_secret = SLACK_SIGNING_SECRET,
    token_verification_enabled=False,
)


@app.event("app_mention")
def handle_app_mentions(logger, event, say):
    try:
        # channel_id = event["channel"]
        # user_id = event["user"]
        message = event["text"]
        response = get_ai_response(message)
        logger.info(f"AI response: {response}")
        say(text=response, thread_ts=event["ts"])

    except Exception as e:
        logger.error(f"Error in handle_app_mentions: {str(e)}")
        say(
            text="Sorry, I encountered an error while processing your request. Please try again.",
            thread_ts=event["ts"]
        )
    # Conversation = apps.get_model("bot", "Conversation")
    # logger.info(event)
    # channel_id = event["channel"]
    # user_id = event["user"]
    # message = event["text"]
    # logger.info(f"Received app mention from {user_id} in {channel_id}: {message}")
    # logger.info("Creating conversation...")
    # qs = Conversation.objects.all()
    # logger.info(f"Conversations: {qs}")
    # previous_conversations = Conversation.objects.filter(
    #     channel_id=channel_id
    # ).order_by('-timestamp')[:5]
    # logger.info(f"Previous conversations: {previous_conversations}")
    # logger.info("Generating AI response...")
    # response = get_ai_response(previous_conversations)
    # logger.info(f"AI response: {response}")
    # Conversation.objects.create(
    #     channel_id=channel_id,
    #     user_id=user_id,
    #     message=message,
    #     response=response
    # )
    # logger.info("Sending response to user...")
    # say(text="Hello, I am a bot. How can I help you?")
