# views.py

from rest_framework import generics
from .models import Usuario, Perfil, Entrada, Comentario, Like
from .serializers import UsuarioSerializer, PerfilSerializer, EntradaSerializer, ComentarioSerializer, LikeSerializer

class UsuarioListCreateView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PerfilListCreateView(generics.ListCreateAPIView):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

class PerfilRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

class EntradaListCreateView(generics.ListCreateAPIView):
    queryset = Entrada.objects.all()
    serializer_class = EntradaSerializer

class EntradaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entrada.objects.all()
    serializer_class = EntradaSerializer

class ComentarioListCreateView(generics.ListCreateAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class ComentarioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class LikeListCreateView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class LikeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


