# urls.py

from django.urls import path
from .views import (
    UsuarioListCreateView, UsuarioRetrieveUpdateDestroyView,
    PerfilListCreateView, PerfilRetrieveUpdateDestroyView,
    EntradaListCreateView, EntradaRetrieveUpdateDestroyView,
    ComentarioListCreateView, ComentarioRetrieveUpdateDestroyView,
    LikeListCreateView, LikeRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('usuarios/', UsuarioListCreateView.as_view(), name='usuario-list'),
    path('usuarios/<int:pk>/', UsuarioRetrieveUpdateDestroyView.as_view(), name='usuario-detail'),
    path('perfiles/', PerfilListCreateView.as_view(), name='perfil-list'),
    path('perfiles/<int:pk>/', PerfilRetrieveUpdateDestroyView.as_view(), name='perfil-detail'),
    path('entradas/', EntradaListCreateView.as_view(), name='entrada-list'),
    path('entradas/<int:pk>/', EntradaRetrieveUpdateDestroyView.as_view(), name='entrada-detail'),
    path('comentarios/', ComentarioListCreateView.as_view(), name='comentario-list'),
    path('comentarios/<int:pk>/', ComentarioRetrieveUpdateDestroyView.as_view(), name='comentario-detail'),
    path('likes/', LikeListCreateView.as_view(), name='like-list'),
    path('likes/<int:pk>/', LikeRetrieveUpdateDestroyView.as_view(), name='like-detail'),
]

