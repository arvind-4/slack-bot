import json
from bot.services.slack import app
from django.views.decorators.csrf import csrf_exempt
from slack_bolt.adapter.django import SlackRequestHandler
from django.http import (HttpResponse, HttpRequest, JsonResponse,)

handler = SlackRequestHandler(app=app)

def hello(request: HttpRequest) -> HttpResponse:
    return JsonResponse({"ping": "pong"})

@csrf_exempt
def slack_events_handler(request: HttpRequest):
    if request.method == "POST":
        body = json.loads(request.body)
        challenge = body.get("challenge")
        if challenge:
            return JsonResponse({"challenge": challenge})
        return handler.handle(request)
    return handler.handle(request)