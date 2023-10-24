from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Produto, Usuario, Compra
from .serializers import ProdutoSerializer, UsuarioSerializer, CompraSerializer

# Create your tests here.

class ProdutoTestes(TestCase):
	def setUp(self):
		self.client = APIClient()
		self.produto_data = {'nome':'Teste', 'preco': 40.00, 'descricao': 'Realizando teste de unidade', 'codigo':'1234567890', 'marca':'tester'}
		self.response = self.client.post(reverse('produto-lista'), self.produto_data, format='json')

	def teste_criar_produto(self):
		self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

	def teste_listar_produto(self):
		produto = Produto.objects.get()
		response = self.client.get(reverse('produto-detalhe', kwargs={'pk':produto.id}), format='json')
		serializer = ProdutoSerializer(produto)
		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def teste_editar_produto(self):
		produto = Produto.objects.get()
		novos_dados = {'nome':'Novo Nome', 'preco':15.00, 'descricao':'Testando a edição do produto', 'codigo':'0987654321', 'marca':'Marca Nova'}
		response = self.client.put(reverse('produto-detalhe', kwargs={'pk':produto.id}), novos_dados, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def teste_deletar_produto(self):
		produto = Produto.objects.get()
		response = self.client.delete(reverse('produto-detalhe', kwargs={'pk':produto.id}))
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class UsuarioTestes(TestCase):
	def setUp(self):
		self.client = APIClient()
		self.usuario_data = {'nome':'Teste da Silva','email':'silva@teste.com','senha':'teste123'}
		self.response = self.client.post(reverse('usuario-lista'),self.usuario_data, format='json')

	def teste_criar_usuario(self):
		self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

	def teste_listar_usuario(self):
		usuario = Usuario.objects.get()
		response = self.client.get(reverse('usuario-detalhe', kwargs={'pk': usuario.id}), format='json')
		serializer = UsuarioSerializer(usuario)
		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def teste_editar_usuario(self):
		usuario = Usuario.objects.get()
		novos_dados = {'nome':'Novo Teste Pereira', 'email':'pereira@testenovo.com','senha':'nova123'}
		response = self.client.put(reverse('usuario-detalhe', kwargs={'pk':usuario.id}), novos_dados, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def teste_deletar_usuario(self):
		usuario = Usuario.objects.get()
		response = self.client.delete(reverse('usuario-detalhe', kwargs={'pk':usuario.id}))
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class CompraTestes(TestCase):
	def setUp(self):
		self.client = APIClient()

	def test_criar_compras(self):
		usuario = Usuario.objects.create(nome='Teste', email='teste@teste.com', senha='teste123')
		produto = Produto.objects.create(nome='Produto Teste', preco=14.00, descricao="Descrição de teste", codigo='12345', marca='Tester')
		data = {'usuario':usuario.id , 'produto':produto.id}
		response = self.client.post(reverse('compra-lista'), data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
