from django.contrib import admin
from galeria.models import Fotografia #, FotografiaCategoria

class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'categoria', 'foto')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'categoria')

# class ListandoFotografiasCategorias(admin.ModelAdmin):
#     list_display = ('id', 'nome')
#     list_display_links = ('id', 'nome')
#     search_fields = ('nome', )

admin.site.register(Fotografia, ListandoFotografias)
# admin.site.register(FotografiaCategoria, ListandoFotografiasCategorias)