import logging
from slack_bolt import App
from django.db import transaction
from bot.models import Conversation
from asgiref.sync import sync_to_async
from bot.services.ai import get_ai_response
from backend.constants import SLACK_BOT_TOKEN, SLACK_SIGNING_SECRET

logger = logging.getLogger(__name__)

app = App(
    token = SLACK_BOT_TOKEN,
    signing_secret = SLACK_SIGNING_SECRET,
    token_verification_enabled=False,
)

@sync_to_async
def save_conversation(channel_id, user_id, message, response) -> None:
    try:
        with transaction.atomic():
            Conversation.objects.create(
                channel_id=channel_id,
                user_id=user_id,
                message=message,
                response=response
            )
            logger.info(f"Conversation saved successfully for channel: {channel_id}")
    except Exception as e:
        logger.error(f"Error saving conversation: {str(e)}")

@sync_to_async
def get_previous_conversations(channel_id):
    try:
        return list(Conversation.objects.filter(
            channel_id=channel_id
        ).order_by('-timestamp')[:5])
    except Exception as e:
        logger.error(f"Error fetching conversations: {str(e)}")
        return []

@app.event("app_mention")
async def handle_app_mentions(logger, event, say):
    try:
        channel_id = event["channel"]
        user_id = event["user"]
        message = event["text"]
        previous_conversations = await get_previous_conversations(channel_id)
        conversation_history = []
        for conv in reversed(previous_conversations):
            conversation_history.append({"role": "user", "content": conv.message})
            conversation_history.append({"role": "assistant", "content": conv.response})
        conversation_history.append({"role": "user", "content": message})
        response = get_ai_response(conversation_history)
        await save_conversation(channel_id, user_id, message, response)
        await say(text=response, thread_ts=event["ts"])
        
    except Exception as e:
        logger.error(f"Error in handle_mention: {str(e)}")
        await say(
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
