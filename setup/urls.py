"""setup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from banco_digital.views.cliente_viewset import ClienteViewSet
from banco_digital.views.saque_viewset import SaqueViewSet
from banco_digital.views.deposito_viewset import DepositoViewSet
from banco_digital.views.transferencia_viewset import TransferenciaViewSet
from banco_digital.views.conta_viewset import ContaViewSet
from banco_digital.views.cliente_enderecos_viewset import ClienteEnderecosViewSet
from banco_digital.views.lista_conta_transacao_viewset import ListaContaTransacaoViewSet


router = routers.DefaultRouter()
router.register(r"cliente", ClienteViewSet, "cliente")
router.register(r"saque", SaqueViewSet, "saque")
router.register(r"deposito", DepositoViewSet, "deposito")
router.register(r"transferencia", TransferenciaViewSet, "transferencia")
router.register(r"conta", ContaViewSet, "conta")
router.register(r"cliente_enderecos", ClienteEnderecosViewSet, "cliente_enderecos")


urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path("conta/<str:conta_cliente>/transacoes", ListaContaTransacaoViewSet.as_view()),
    path("api-auth/", include("rest_framework.urls")),
]
