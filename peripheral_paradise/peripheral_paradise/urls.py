"""peripheral_paradise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pp_app.views import ProdutoLista, ProdutoDetalhe, UsuarioLista, UsuarioDetalhe, CompraLista, CompraDetalhe

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produtos/', ProdutoLista.as_view(), name='produto-lista'),
    path('produtos/<int:pk>/', ProdutoDetalhe.as_view(), name='produto-detalhe'),
    path('usuarios/', UsuarioLista.as_view(), name='usuario-lista'),
    path('usuarios/<int:pk>/', UsuarioDetalhe.as_view(), name='usuario-detalhe'),
    path('compras/', CompraLista.as_view(), name='compra-lista'),
    path('compras/<int:pk>', CompraDetalhe.as_view(), name='compra-detalhe'),
]
