from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CandidatoViewSet, PartidoViewSet, ResultadoViewSet, ChatGPTView
from django.http import JsonResponse

def api_home(request):
    return JsonResponse({"message": "API de scraper funcionando correctamente"})

router = DefaultRouter()
router.register(r'candidatos', CandidatoViewSet)
router.register(r'partidos', PartidoViewSet)
router.register(r'resultados', ResultadoViewSet)

urlpatterns = [
    path('', api_home, name='api_home'),
    path('chatgpt/', ChatGPTView.as_view(), name='chatgpt'),
]

urlpatterns += router.urls