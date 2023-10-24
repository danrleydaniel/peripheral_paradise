from django.db import models

# Create your models here.

class Produto(models.Model):
	nome = models.CharField(max_length=300)
	preco = models.FloatField()
	descricao = models.TextField()
	codigo = models.CharField(max_length=10)
	marca = models.CharField(max_length=30)

	def __str__(self):
		return str([self.nome, self.preco, self.descricao, self.codigo, self.marca])

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Compra(models.Model):
	usuario = models.ForeignKey('Usuario',on_delete=models.CASCADE)
	produto = models.ForeignKey('Produto',on_delete=models.CASCADE)
	data_compra = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.usuario} comprou {self.produto} em {self.data_compra}'
