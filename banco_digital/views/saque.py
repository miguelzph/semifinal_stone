from rest_framework import viewsets
from banco_digital.models.transacao import Transacao
from banco_digital.serializer.saque import SaqueSerializer


class SaqueViewSet(viewsets.ModelViewSet):
    queryset = Transacao.objects.all()
    serializer_class = SaqueSerializer