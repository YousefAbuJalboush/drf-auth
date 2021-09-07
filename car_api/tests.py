from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Car
from django.urls import reverse
from rest_framework.test import APITestCase

# Create your tests here.
class CarsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()
        test_post = Car.objects.create(author=testuser1, modelCar='Test Post Body', description='Test Post Body' )
        test_post.save()

    def test_blog_content(self):
        post = Car.objects.get(id = 1)
        expected_auther = f'{post.author}'
        expected_modelCar = f'{post.modelCar}'
        expected_description = f'{post.description}'
        self.assertEqual(expected_auther, 'testuser1')
        self.assertEqual(expected_modelCar, 'Test Post Body')
        self.assertEqual(expected_description, 'Test Post Body')

class APITest(APITestCase):
        def test_auth_list(self):
            response = self.client.get(reverse('cars_list'))
            self.assertEqual(response.status_code, 401)