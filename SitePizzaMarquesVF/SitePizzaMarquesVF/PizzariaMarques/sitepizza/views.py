from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Produto, Pedido, ProdutoPedido, Perfil, Checkout
from .forms import CreateUserForm, PerfilForm
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.contrib import messages
from django.core.files.storage import FileSystemStorage


def home(request):
    if request.user.is_authenticated:
        perfil= Perfil.objects.get(user=request.user)
        return render(request, 'sitepizza/home.html', {'perfil':perfil})
    return render(request, 'sitepizza/home.html')


def sobrenos(request):
    return render(request, 'sitepizza/sobrenos.html')


def finalizar(request):
    if request.user.is_authenticated:

        user = request.user
        pedido = Pedido.objects.get(user=user, ordered=False)
        produtos_pedido = pedido.produtos.all()
        perfil = Perfil.objects.get(user=user)

        if len(produtos_pedido) == 0:
            messages.warning(request, 'Não possui produtos no carrinho.')
            return render(request, 'sitepizza/checkout.html', {'produtos_pedido': produtos_pedido, 'pedido': pedido
                , 'perfil':perfil,})



        checkout = Checkout.objects.create(pedido=pedido)

        try:
            checkout = Checkout.objects.create(pedido=pedido, metEntrega=request.POST['entrega']
                                               , morada=request.POST['morada'], metPagamento= request.POST['pagamento'])

        except (KeyError, Checkout.DoesNotExist):

            messages.warning(request, 'Preencha os campos todos para finalizar.')
            return render(request, 'sitepizza/checkout.html', {'produtos_pedido': produtos_pedido, 'pedido': pedido
                , 'perfil':perfil,})

        else:


            if checkout.morada == "morada2" :
                moradanova_selecionada = request.POST['morada-nova']
                if moradanova_selecionada == '' :
                    messages.warning(request, 'Preencha os campos todos para finalizar.')
                    return render(request, 'sitepizza/checkout.html',
                                  {'produtos_pedido': produtos_pedido, 'pedido': pedido
                                      , 'perfil': perfil, })
                else:

                    checkout.morada = moradanova_selecionada
                    checkout.save()




            produtos_pedidos = ProdutoPedido.objects.filter(user=user, ordered= False)

            pedido.valorPedido = request.POST['subtotal']
            pedido.ordered = True
            pedido.save()

            for produto_pedido in produtos_pedidos :
                produto_pedido.ordered = True
                produto_pedido.save()


            return render(request, 'sitepizza/finalizar.html', {'checkout': checkout , 'pedido': pedido})
    else:
        return redirect(reverse('navegar:login'))



def menu(request):

        # buscar cada produto de cada categoria
    pizzas= Produto.objects.filter(categoria__nome__contains="pizza")
    acompanhamentos= Produto.objects.filter(categoria__nome__contains="acompanhamento")
    bebidas= Produto.objects.filter(categoria__nome__contains="bebida")
    sobremesas= Produto.objects.filter(categoria__nome__contains="sobremesa")

    #por no contexto

    context = {
        'pizzas': pizzas,
        'acompanhamentos': acompanhamentos,
        'bebidas': bebidas,
        'sobremesas': sobremesas,
    }

    #fazer render
    return render(request, 'sitepizza/menu.html', context)


def add_carrinho(request):
    if request.user.is_authenticated:
        produto = Produto.objects.get(pk=request.POST['produto'])
        qtd = int(request.POST['quantidade'])

        produto_pedido, created= ProdutoPedido.objects.get_or_create(produto=produto, user=request.user, ordered=False)

        try:
            pedido = Pedido.objects.get(user= request.user, ordered=False)
        except Pedido.DoesNotExist:

            dataPedido = timezone.now()
            pedido = Pedido.objects.create(user=request.user, dataPedido=dataPedido)
            pedido.produtos.add(produto_pedido)
            produto_pedido.quantidade += qtd
            produto_pedido.save()
            pedido.countprodutos += qtd

            messages.success(request, 'Produto adicionado ao carrinho.')
            return redirect(reverse('navegar:menu'))

        else:

            if pedido.produtos.filter(produto__id=produto.id).exists():
                produto_pedido.quantidade += qtd
                produto_pedido.save()
                pedido.countprodutos += qtd
                pedido.save()

                messages.success(request, 'Produto adicionado ao carrinho.')
                return redirect(reverse('navegar:menu'))
            else:
                pedido.produtos.add(produto_pedido)
                produto_pedido.quantidade += qtd
                produto_pedido.save()
                pedido.countprodutos += qtd
                pedido.save()
                messages.success(request, 'Produto adicionado ao carrinho.')
                return redirect(reverse('navegar:menu'))
    else:
        return redirect(reverse('navegar:login'))


def remove_do_carrinho(request):
    produtopedido_selecionado = ProdutoPedido.objects.get(produto=request.POST['produtopizza'], user=request.user, ordered=False)

    if produtopedido_selecionado.quantidade == 1 :
        produtopedido_selecionado.delete()
        messages.error(request, 'Produto removido.')
        return redirect(reverse('navegar:checkout'))
    else:

        produtopedido_selecionado.quantidade -= 1
        produtopedido_selecionado.save()
        messages.error(request, 'Produto removido.')
        return redirect(reverse('navegar:checkout'))


def checkout(request):
    if request.user.is_authenticated:
        user = request.user
        perfil = Perfil.objects.get(user=user)
        try:
            pedido = Pedido.objects.get(user=user, ordered=False)
        except Pedido.DoesNotExist:
            dataPedido = timezone.now()
            pedido = Pedido.objects.create(user=request.user, dataPedido=dataPedido)
            produtos_pedido = pedido.produtos.all()
            for produto in produtos_pedido :
                print(produto)
            return render(request, 'sitepizza/checkout.html', {'produtos_pedido': produtos_pedido, 'pedido': pedido
                , 'perfil':perfil,})

        else:
            produtos_pedido = pedido.produtos.all()
            for produto in produtos_pedido :
                print(produto)

            return render(request, 'sitepizza/checkout.html', {'produtos_pedido': produtos_pedido, 'pedido': pedido
                , 'perfil':perfil,})

    else:
        return redirect(reverse('navegar:login'))


#--------------------------LOGIN / REGISTO-------------------------------------------------------------


def registo(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        perfil_form = PerfilForm(request.POST)

        if form.is_valid() and perfil_form.is_valid():
            user = form.save()
            perfil = perfil_form.save(commit=False)
            perfil.user = user
            perfil.save()

            user = form.cleaned_data.get('username')
            messages.success(request,'A conta foi criada para ' + user)
            return HttpResponseRedirect('login')
    else:
        form = CreateUserForm()
        perfil_form = PerfilForm()
    return render(request, 'sitepizza/registo.html', {'form':form, 'perfil_form': perfil_form} )



def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('home')
        else:
            messages.info(request, 'Username ou Password Incorreta!')


    context = {}
    return render(request, 'sitepizza/login.html', context)


def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('login')


#---------------------------------------Perfil--------------------------------------------------------------------------

def perfil(request, user_id):
    perfil = Perfil.objects.get(user=request.user)
    return render(request, 'sitepizza/perfil.html', {'perfil': perfil })

def fazer_upload(request):
        user= request.user
        perfil = Perfil.objects.get(user=user)
        myfile = request.FILES['myfile']
        perfil.image = myfile
        perfil.save()

        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'sitepizza/perfil.html', {'uploaded_file_url': uploaded_file_url, 'perfil': perfil})