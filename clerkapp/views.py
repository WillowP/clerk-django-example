from django.http import JsonResponse

def clerk_jwt(request):
    if request.clerk_user is None:
        return JsonResponse({'userId': None})
    return JsonResponse({'userId': request.clerk_user['sub']})
