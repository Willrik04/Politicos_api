from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CandidatoViewSet, PartidoViewSet, ResultadoViewSet, ChatGPTView

router = DefaultRouter()
router.register(r'candidatos', CandidatoViewSet)
router.register(r'partidos', PartidoViewSet)
router.register(r'resultados', ResultadoViewSet)

urlpatterns = [
    path('chatgpt/', ChatGPTView.as_view(), name='chatgpt'),
]

urlpatterns += router.urls