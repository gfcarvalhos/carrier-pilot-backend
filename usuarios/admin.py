from django.contrib import admin
from usuarios.models import Usuario, Perfil, Habilidade

class Usuarios(admin.ModelAdmin):
  list_display=('id','nome','email','data_cadastro','tipo_usuario')
  list_display_links=('id', 'nome')
  list_per_page=20
  search_fields=('nome', 'tipo_usuario')
  ordering=('id',)
admin.site.register(Usuario, Usuarios)

class Perfils(admin.ModelAdmin):
  list_display=('id','usuario','area_interesse','nivel_experiencia','objetivo_pessoal')
  list_display_links=('id', 'usuario')
  list_per_page=20
  search_fields=('usuario__username', 'usuario__email' , 'usuario__id', 'nivel_experiencia')
  ordering=('id',)
admin.site.register(Perfil, Perfils)

class Habilidades(admin.ModelAdmin):
  list_display=('id','nome','descricao',)
  list_display_links=('id', 'nome')
  list_per_page=20
  search_fields=( 'nome',)
  ordering=('id',)
admin.site.register(Habilidade, Habilidades)
