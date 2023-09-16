from rest_framework import generics
from .models import Produto, Usuario
from .serializers import ProdutoSerializer, UsuarioSerializer

# Create your views here.

class ProdutoLista(generics.ListCreateAPIView):
	queryset = Produto.objects.all()
	serializer_class = ProdutoSerializer

class ProdutoDetalhe(generics.RetrieveUpdateDestroyAPIView):
	queryset = Produto.objects.all()
	serializer_class = ProdutoSerializer

class UsuarioLista(generics.ListCreateAPIView):
	queryset = Usuario.objects.all()
	serializer_class = UsuarioSerializer

class UsuarioDetalhe(generics.RetrieveUpdateDestroyAPIView):
	queryset = Usuario.objects.all()
	serializer_class = UsuarioSerializer