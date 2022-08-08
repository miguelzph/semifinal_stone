from django.test import TestCase

# Create your tests here.

class ExemploTestCase(TestCase):
    
    def test_exemplo(self):
        a = 2
        b = 2
        self.assertTrue(a == 3)
