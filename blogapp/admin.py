from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria


class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = 'nombre', 'fecha_crate', 'estado'
    resource_class = CategoriaResource


class AutorResource(resources.ModelResource):
    class Meta:
        models = Autor


class AutorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['Nombres', 'Apellidos']
    list_display = 'Nombres', 'Apellidos', 'email', 'fecha_create'


class PostAdmin(admin.ModelAdmin):
    list_display = 'titulo', 'autor', 'categoria'


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Post, PostAdmin)
