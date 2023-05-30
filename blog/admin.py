from django.contrib import admin
from .models import Usuario, Perfil, Entrada, Comentario, Like

admin.site.register(Usuario)
admin.site.register(Perfil)
admin.site.register(Entrada)
admin.site.register(Comentario)
admin.site.register(Like)


