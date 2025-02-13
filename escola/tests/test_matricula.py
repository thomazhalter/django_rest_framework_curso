from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

class MatriculaTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin',password='admin') 
        self.url = reverse('Matriculas-list')
        self.client.force_authenticate(user = self.usuario)

    def test_requisicao_delete_uma_matricula(self):
        """Teste de requisição DELETE uma matricula"""
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code,status.HTTP_405_METHOD_NOT_ALLOWED)