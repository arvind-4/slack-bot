from bot.services.slack import app
from django.views.decorators.csrf import csrf_exempt
from slack_bolt.adapter.django import SlackRequestHandler
from django.http import (HttpResponse, HttpRequest, JsonResponse,)

handler = SlackRequestHandler(app=app)

def hello(request: HttpRequest) -> HttpResponse:
    return JsonResponse({"ping": "pong"})

@csrf_exempt
async def slack_events_handler(request):
    try:
        return await handler.handle(request)
    except Exception as e:
        # logger.error(f"Error handling Slack event: {str(e)}")
        print(e)
        return HttpResponse(status=500)
    