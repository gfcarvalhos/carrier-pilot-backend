from django.contrib import admin
from django.urls import path, include
from usuarios.views import UsuarioViewSet, PerfilViewSet
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('usuarios', UsuarioViewSet, basename='usuarios')
routers.register('perfis',PerfilViewSet, basename='perfis')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(routers.urls))
]
