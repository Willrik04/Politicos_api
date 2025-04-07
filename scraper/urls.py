from django.urls import path
from django.http import JsonResponse

def api_home(request):
    return JsonResponse({"message": "API de scraper funcionando correctamente"})

urlpatterns = [
    path('', api_home, name='api_home'),
]