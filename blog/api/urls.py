# api/urls.py

from django.urls import path
from .views import UsuarioListCreateView, UsuarioRetrieveUpdateDestroyView, PerfilListCreateView, PerfilRetrieveUpdateDestroyView, EntradaListCreateView, EntradaRetrieveUpdateDestroyView, ComentarioListCreateView, ComentarioRetrieveUpdateDestroyView, LikeListCreateView, LikeRetrieveUpdateDestroyView

urlpatterns = [
    path('usuarios/', UsuarioListCreateView.as_view(), name='usuario-list-create'),
    path('usuarios/<int:pk>/', UsuarioRetrieveUpdateDestroyView.as_view(), name='usuario-retrieve-update-destroy'),
    path('perfiles/', PerfilListCreateView.as_view(), name='perfil-list-create'),
    path('perfiles/<int:pk>/', PerfilRetrieveUpdateDestroyView.as_view(), name='perfil-retrieve-update-destroy'),
    path('entradas/', EntradaListCreateView.as_view(), name='entrada-list-create'),
    path('entradas/<int:pk>/', EntradaRetrieveUpdateDestroyView.as_view(), name='entrada-retrieve-update-destroy'),
    path('comentarios/', ComentarioListCreateView.as_view(), name='comentario-list-create'),
    path('comentarios/<int:pk>/', ComentarioRetrieveUpdateDestroyView.as_view(), name='comentario-retrieve-update-destroy'),
    path('likes/', LikeListCreateView.as_view(), name='like-list-create'),
    path('likes/<int:pk>/', LikeRetrieveUpdateDestroyView.as_view(), name='like-retrieve-update-destroy'),
]
