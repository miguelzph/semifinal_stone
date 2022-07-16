from rest_framework import viewsets
from rest_framework import mixins
from banco_digital.models.conta import Conta
from banco_digital.serializer.conta_serializer import ContaSerializer


class ContaViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    """ViewSet que permite visualizer a lista de contas da base."""

    queryset = Conta.objects.all()
    serializer_class = ContaSerializer
