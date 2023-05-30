# models.py

from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    ROLES = (
        ('administrador', 'Administrador'),
        ('editor', 'Editor'),
        ('blogger', 'Blogger'),
    )
    
    rol = models.CharField(max_length=15, choices=ROLES)


class Perfil(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='perfil')
    biografia = models.TextField(blank=True)
    imagen_perfil = models.ImageField(upload_to='perfil/', blank=True)


class Entrada(models.Model):
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='entradas')
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    categoria = models.CharField(max_length=255)
    etiquetas = models.ManyToManyField('Etiqueta', related_name='entradas')


class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='comentarios')
    entrada = models.ForeignKey(Entrada, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='likes')
    entrada = models.ForeignKey(Entrada, on_delete=models.CASCADE, related_name='likes')
    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE, related_name='likes', null=True)


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=255)
