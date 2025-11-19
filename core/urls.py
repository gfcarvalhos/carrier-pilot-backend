from django.contrib import admin
from django.urls import path, include
from usuarios.views import UsuarioViewSet, PerfilViewSet, HabilidadeViewSet
from carreiras.views import AtividadeViewSet, RecomendacaoViewSet, ProgressoViewSet
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('usuarios', UsuarioViewSet, basename='usuarios')
routers.register('perfis',PerfilViewSet, basename='perfis')
routers.register('habilidades', HabilidadeViewSet, basename='habilidades')
routers.register('atividades', AtividadeViewSet, basename='atividades')
routers.register('recomendacoes', RecomendacaoViewSet, basename='recomendacoes')
routers.register('progresso', ProgressoViewSet, basename='progresso')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(routers.urls)),
    path('carreiras/', include('carreiras.urls'))
]
