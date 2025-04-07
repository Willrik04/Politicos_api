from django.contrib import admin
from django.urls import path
from django.http import JsonResponse

def home_view(request):
    return JsonResponse({"message": "API funcionando correctamente"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    # Comentamos temporalmente la línea problemática
    # path('api/', include('scraper.urls')),
]