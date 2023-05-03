from django.contrib import admin
from galeria.models import Fotografia, Categoria

class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria', 'ativo')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'categoria')
    list_filter = ("categoria", )
    list_editable = ("ativo", )
    list_per_page = 15


class ListandoCategorias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'ativo')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', )
    list_editable = ("ativo", )
    list_per_page = 15


admin.site.register(Fotografia, ListandoFotografias)
admin.site.register(Categoria, ListandoCategorias)