from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('candidatos/', views.CandidatoListView.as_view(), name='candidato-list'),
    path('candidatos/<int:pk>/', views.CandidatoDetailView.as_view(), name='candidato-detail'),
    path('partidos/', views.PartidoListView.as_view(), name='partido-list'),
    path('partidos/<int:pk>/', views.PartidoDetailView.as_view(), name='partido-detail'),
    path('resultados/', views.ResultadoElectoralListView.as_view(), name='resultado-list'),
    path('chatgpt/', views.ChatGPTView.as_view(), name='chatgpt'),
]