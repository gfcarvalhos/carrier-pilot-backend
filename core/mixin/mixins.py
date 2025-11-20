from rest_framework.exceptions import PermissionDenied

class UniversalUserFilterMixin:
    """
    Mixin para que usuários comuns acessem apenas seus próprios registros
    e superusuários acessem tudo.
    """
    def get_queryset(self):
        queryset = super().get_queryset()
        user_django = self.request.user

        if user_django.is_superuser:
            return queryset
        
        try:
            usuario = user_django.usuario
        except:
            return queryset.none()
        
        return queryset.filter(usuario=usuario)

class IndirectUserFilterMixin:
    """
    Filtra objetos relacionados ao usuário via outra FK:
        objeto.recomendacao.usuario
    """
    user_relation = None
    
    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user

        if not self.user_relation:
            return queryset.none()

        return queryset.filter(**{self.user_relation: user.usuario})


class OwnUserDataMixin:
    owner_field = "user"

    def get_queryset(self):
        qs = super().get_queryset()

        if self.request.user.is_superuser:
            return qs
        
        filtro = {self.owner_field: self.request.user}
        return qs.filter(**filtro)

    def perform_create(self, serializer):
        if not self.request.user.is_superuser:
            serializer.save(**{self.owner_field: self.request.user})
        else:
            serializer.save()

class RestrictToSelfMixin:
    def get_queryset(self):
        qs = super().get_queryset()

        if self.request.user.is_superuser:
            return qs
        return qs.filter(id=self.request.user.id)