import logging
from slack_bolt import App
from backend.constants import SLACK_BOT_TOKEN, SLACK_SIGNING_SECRET

logger = logging.getLogger(__name__)

app = App(
    token = SLACK_BOT_TOKEN,
    signing_secret = SLACK_SIGNING_SECRET,
    token_verification_enabled=False,
)

@app.event("app_mention")
def handle_app_mentions(logger, event, say):
    logger.info(event)
    say(f"Hi there, <@{event['user']}>")