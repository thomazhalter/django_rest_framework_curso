from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

class CursoTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin',password='admin') 
        self.url = reverse('Cursos-list')
        self.client.force_authenticate(user = self.usuario)

    def test_requisicao_delete_um_curso(self):
        """Teste de requisição DELETE um curso"""
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)