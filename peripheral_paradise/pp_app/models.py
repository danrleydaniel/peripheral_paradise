from django.db import models

# Create your models here.

class Produto(models.Model):
	nome = models.CharField(max_length=300)
	preco = models.FloatField()
	descricao = models.TextField()
	codigo = models.CharField(max_length=10)
	marca = models.CharField(max_length=30)

	def __str__(self):
		return [self.nome, self.preco, self.descricao, self.codigo, self.marca]

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.nome