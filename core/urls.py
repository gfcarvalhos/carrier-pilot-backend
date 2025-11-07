from django.contrib import admin
from django.urls import path, include
from usuarios.views import UsuarioViewSet, PerfilViewSet, HabilidadeViewSet
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('usuarios', UsuarioViewSet, basename='usuarios')
routers.register('perfis',PerfilViewSet, basename='perfis')
routers.register('habilidades', HabilidadeViewSet, basename='habilidades')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(routers.urls))
]
