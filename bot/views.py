from bot.services.slack import handler
from django.views.decorators.csrf import csrf_exempt
from django.http import (HttpResponse, HttpRequest, JsonResponse,)

def hello(request: HttpRequest) -> HttpResponse:
    return JsonResponse({"ping": "pong"})

@csrf_exempt
def slack_events(request: HttpRequest) -> HttpResponse:
    return HttpResponse(handler.handle(request))