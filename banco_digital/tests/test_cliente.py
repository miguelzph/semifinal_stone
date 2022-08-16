from django.test import TestCase
from rest_framework.test import APIClient


class CreateClienteTestCase(TestCase):
    def test_exemplo(self):
        client = APIClient()

        data_cliente = {
            "nome": "Juarez da Silva",
            "cpf": "23623777099",
            "email": "juarez@gmail.com",
            "telefone": "9889858849",
            "tipo": "PF",
        }

        response = client.post("/cliente/", data_cliente, format="json")

        data_cliente["conta"] = 100001

        self.assertTrue(response.status_code == 201)
        self.assertTrue(response.json() == data_cliente)
