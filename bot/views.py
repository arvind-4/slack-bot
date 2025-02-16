import json
from bot.services.slack import handler
from django.views.decorators.csrf import csrf_exempt
from django.http import (HttpResponse, HttpRequest, JsonResponse,)

def hello(request: HttpRequest) -> HttpResponse:
    return JsonResponse({"ping": "pong"})

@csrf_exempt
def slack_events(request: HttpRequest) -> HttpResponse:
    # return HttpResponse(handler.handle(request))
    body = json.loads(request.body)
    challenge = body.get('challenge')
    if challenge:
        return JsonResponse({'challenge': challenge})
    return JsonResponse({'challenge': None})
