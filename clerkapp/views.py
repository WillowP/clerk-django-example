from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from clerk_backend_api.jwks_helpers import verify_token, VerifyTokenOptions

from urllib.request import urlopen
import json

def clerk_jwt(request):
    # Strip the "Bearer " prefix from the header
    token = request.headers['Authorization'][7:]
    decoded = verify_token(token, VerifyTokenOptions(secret_key=settings.CLERK_SECRET_KEY))
    data =  {
        'userId': decoded['sub'],
    }
    return JsonResponse(data)