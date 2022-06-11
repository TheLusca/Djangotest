from django.db import models

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preco', decimal_places=2, max_digits=8)
    estoqque = models.IntegerField('Quantidade em estoque')


# quando apresentar o obnjeto apresenta o nome peol qual foi criado

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('Email', max_length=100)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
