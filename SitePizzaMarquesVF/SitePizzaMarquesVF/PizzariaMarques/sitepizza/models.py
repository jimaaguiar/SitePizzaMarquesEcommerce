from django.contrib.auth.models import User
from django.db import models

BIG_CHAR = 100
MEDIUM_CHAR = 50
SMALL_CHAR = 25
DINHEIRO = 5
DECIMAL = 2
ID = 3


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    morada = models.TextField(null=True, max_length= MEDIUM_CHAR)
    telemovel = models.IntegerField(null=True)
    image= models.ImageField(upload_to='media', null=True)


class Categoria(models.Model):
    nome= models.CharField(max_length=BIG_CHAR)
    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=BIG_CHAR, null=False)
    descricao= models.TextField(null=True, blank=True)
    image= models.ImageField(upload_to='media')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    preco = models.DecimalField(default=0, decimal_places=2, max_digits=5)


    def __str__(self):
        return self.nome




class ProdutoPedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.quantidade} de {self.produto.nome}"

    def precoprodutos(self):
        return self.quantidade*self.produto.preco;


class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    valorPedido = models.FloatField(default=0)
    dataPedido = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=SMALL_CHAR, null=False)
    ordered = models.BooleanField(default=False)
    produtos = models.ManyToManyField(ProdutoPedido)
    countprodutos= models.IntegerField(default=0)

    def __str__(self):
        return '{0} - {1}'.format(self.user, self.id)


    def subtotal(self):
        return sum([ (produtoitem.quantidade*produtoitem.produto.preco)   for produtoitem in self.produtos.all()])


class Checkout(models.Model):
    metEntrega= models.TextField(null=True, max_length=MEDIUM_CHAR)
    morada = models.TextField(null=True, max_length=MEDIUM_CHAR)
    metPagamento = models.TextField(null=True, max_length=MEDIUM_CHAR)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
