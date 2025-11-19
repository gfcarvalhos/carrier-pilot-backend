import django_filters
from usuarios.models import Perfil

class PerfilFilter(django_filters.FilterSet):
    usuario__nome = django_filters.CharFilter(
        field_name='usuario__nome', lookup_expr='icontains'
    )
    usuario__email = django_filters.CharFilter(
        field_name='usuario__email', lookup_expr='icontains'
    )

    class Meta:
        model = Perfil
        fields = ['nivel_experiencia', 'usuario__nome', 'usuario__email']
