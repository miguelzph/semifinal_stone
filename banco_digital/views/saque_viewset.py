from rest_framework import viewsets
from banco_digital.models.transacao import Transacao
from banco_digital.models.status_transacao import StatusTransacao
from banco_digital.models.tipo_transacao import TipoTransacao
from banco_digital.serializer.saque_serializer import SaqueSerializer
from rest_framework.response import Response


class SaqueViewSet(viewsets.ModelViewSet):
    queryset = Transacao.objects.all()
    serializer_class = SaqueSerializer
    
    def perform_create(self, serializer):
        serializer.save(tipo_id=TipoTransacao.objects.get(id=1), 
                        status_id=StatusTransacao.objects.get(id=1))
     
        
    

