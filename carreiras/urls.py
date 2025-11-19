from django.urls import path
from carreiras.views import GerarRoadMapView

urlpatterns = [
    path('gerar/', GerarRoadMapView.as_view(), name='gerar_recomendacao'),
]
