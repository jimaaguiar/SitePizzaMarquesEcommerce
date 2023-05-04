from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'navegar'
urlpatterns = [
 path("", views.home, name="home"),
 path("home", views.home, name="home"),
 path("menu", views.menu, name="menu"),
 path("perfil/<int:user_id>", views.perfil, name="perfil"),
 path("sobrenos", views.sobrenos, name="sobrenos"),
 path("menu/checkout", views.checkout, name="checkout"),
 path("registo", views.registo, name="registo"),
 path("login", views.loginPage, name="login"),
 path("logout", views.logoutUser, name="logout"),
 path("add_carrinho", views.add_carrinho, name="add_carrinho"),
 path("remove_do_carrinho", views.remove_do_carrinho, name="remove_do_carrinho"),
 path("checkout/finalizar", views.finalizar, name="finalizar"),
 path('fazer_upload', views.fazer_upload, name='fazer_upload'),
]

if settings.DEBUG:
 urlpatterns += static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)