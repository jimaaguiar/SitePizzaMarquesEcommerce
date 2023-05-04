from django.contrib import admin
from .models import Produto, Pedido, ProdutoPedido, Categoria, Checkout, Perfil
# Register your models here.
admin.site.register(Produto)
admin.site.register(Pedido)
admin.site.register(Perfil)
admin.site.register(Categoria)
admin.site.register(ProdutoPedido)
admin.site.register(Checkout)


