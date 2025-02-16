import json
from bot.services.slack import app
from bot.models import Conversation
from django.views.decorators.csrf import csrf_exempt
from slack_bolt.adapter.django import SlackRequestHandler
from django.http import (HttpResponse, HttpRequest, JsonResponse,)

handler = SlackRequestHandler(app=app)

def hello(request: HttpRequest) -> HttpResponse:
    qs = Conversation.objects.all()
    print(qs)
    return JsonResponse({"ping": "pong"})

@csrf_exempt
def slack_events_handler(request: HttpRequest):
    return handler.handle(request)