from django.contrib import admin
from usuarios.models import Usuario, Perfil

class Usuarios(admin.ModelAdmin):
  list_display=('id','nome','email','data_cadastro','tipo_usuario')
  list_display_links=('id', 'nome')
  list_per_page=20
  search_fields=('nome', 'tipo_usuario')
  ordering=('nome',)
admin.site.register(Usuario, Usuarios)

class Perfils(admin.ModelAdmin):
  list_display=('id','usuario','area_interesse','nivel_experiencia','objetivo_pessoal')
  list_display_links=('id', 'usuario')
  list_per_page=20
  search_fields=('usuario', 'nivel_experiencia')
  ordering=('id',)
admin.site.register(Perfil, Perfils)
