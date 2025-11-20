from rest_framework.exceptions import PermissionDenied

class UniversalUserFilterMixin:
    """
    Mixin para que usuários comuns acessem apenas seus próprios registros
    e superusuários acessem tudo.
    """
    def get_queryset(self):
        #Swagger building only
        if getattr(self, "swagger_fake_view", False):
            return super().get_queryset()

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
        #Swagger building only
        if getattr(self, "swagger_fake_view", False):
            return super().get_queryset()

        queryset = super().get_queryset()
        user = self.request.user

        if not self.user_relation:
            return queryset.none()

        return queryset.filter(**{self.user_relation: user.usuario})


class OwnUserDataMixin:
    owner_field = "usuario"

    def get_queryset(self):
        #Swagger building only
        if getattr(self, "swagger_fake_view", False):
            return super().get_queryset()

        qs = super().get_queryset()
        django_user = self.request.user

        if django_user.is_superuser:
            return qs
        try:
            usuario = django_user.usuario
        except:
            return qs.none()
        
        filtro = {self.owner_field: usuario}
        return qs.filter(**filtro)

    def perform_create(self, serializer):
        django_user = self.request.user
        if not django_user.is_superuser:
            serializer.save(**{self.owner_field: django_user.usuario})
        else:
            serializer.save()

class RestrictToSelfMixin:
    def get_queryset(self):
        #Swagger building only
        if getattr(self, "swagger_fake_view", False):
            return super().get_queryset()
        
        qs = super().get_queryset()

        if self.request.user.is_superuser:
            return qs
        return qs.filter(user=self.request.user)