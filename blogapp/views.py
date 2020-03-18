from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator


def index(request):
    posts = Post.objects.filter(estado=True)
    query = request.GET.get("buscar")
    if query:
        posts = Post.objects.filter(
            Q(titulo__icontains = query) |
            Q(descripcion__icontains = query)
            ).distinct()

    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'index.html', {'posts': posts})


def DetallePost(req, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(req, 'post.html', {'post': post})
    """autor = """


def Generales(req):
    posts = Post.objects.filter(
        estado=True, 
        categoria=Categoria.objects.get(nombre='General'))
    return render(req, 'generales.html', {'posts': posts})


def Programacion(req):
    posts = Post.objects.filter(
        estado=True, 
        categoria=Categoria.objects.get(nombre='Programación'))
    return render(req, 'programacion.html', {'posts': posts})


def Juegos(req):
    posts = Post.objects.filter(
        estado=True, 
        categoria=Categoria.objects.get(nombre='Juegos'))
    return render(req, 'juegos.html', {'posts': posts})


def Contactos(req):
    posts = Post.objects.filter(
        estado=True, 
        categoria=Categoria.objects.get(nombre='Contactos'))
    return render(req, 'contactos.html', {'posts': posts})
