from django.contrib import admin
from django.urls import path, include
from usuarios.views import UsuarioViewSet, PerfilViewSet, HabilidadeViewSet
from carreiras.views import AtividadeViewSet, RecomendacaoViewSet, ProgressoViewSet
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Documentação da API Carrier Pilot",
      default_version='v1',
      description="Documentação da API Carrier Pilot",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="gabrielfelipecarvalho1@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

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
    path('carreiras/', include('carreiras.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
