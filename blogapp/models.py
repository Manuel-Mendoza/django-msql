from django.db import models
from ckeditor.fields import RichTextField


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    estado = models.BooleanField(default=True)
    fecha_crate = models.DateField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre


class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    Nombres = models.CharField(max_length=30, null=False, blank=False)
    Apellidos = models.CharField(max_length=30, null=False, blank=False)
    facebook = models.URLField(max_length=200, null=True, blank=True)
    twitter = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)
    page_web = models.URLField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=254, null=False, blank=False)
    estado = models.BooleanField(default=True)
    fecha_create = models.DateField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return "{0},{1}".format(self.Apellidos, self.Nombres)


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField("Titulo del Post", max_length=50, null=False,blank=False)
    slug = models.CharField("slug", max_length=50, null=False, blank=False)
    descripcion = models.CharField(max_length=100, null=False, blank=False)
    contenido = RichTextField()
    imagen = models.URLField(max_length=200, blank=False, null=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.BooleanField('Estado', default=True)
    fecha_Create = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Publicaciones'

    def __str__(self):
        return self.titulo
