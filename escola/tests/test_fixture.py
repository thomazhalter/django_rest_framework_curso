from django.test import TestCase
from escola.models import Estudante, Curso

class FixturesTestCase(TestCase):
    fixtures = ['prototipo_banco.json']

    def test_carregamento_da_fixture(self):
        """"Teste que verifica o carregamento da fixtures"""
        estudante = Estudante.objects.get(cpf = '46296117116')
        curso = Curso.objects.get(pk=1)
        self.assertEqual (estudante.celular, '36 98692-4954')
        self.assertEqual(curso.codigo, 'POO')