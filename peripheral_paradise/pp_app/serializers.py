from rest_framework import serializers
from .models import Produto, Usuario, Compra

class ProdutoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Produto
		fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Usuario
		fields = '__all__'

class CompraSerializer(serializers.ModelSerializer):
	class Meta:
		model = Compra
		fields = '__all__'
