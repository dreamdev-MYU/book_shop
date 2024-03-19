from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

class RegisterTestCase(TestCase):

    def test_register(self):
        response = self.client.post(
            reverse('users:register'),  
            data={
                'username': 'bookshop',
                'first_name': 'Bekxan',
                'last_name': 'mekhmonaliev',
                'email': 'mekhmonaliev@gmail.com',
                'password': '0906',
                'confirm_password': '0906',  
            }
        )
        self.assertEqual(response.status_code, 302) 
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)

        user = User.objects.get(username='bookshop')
        self.assertEqual(user.first_name, 'Bekxan')
        self.assertEqual(user.last_name, 'mekhmonaliev')
        self.assertEqual(user.email, 'mekhmonaliev@gmail.com')
        self.assertTrue(user.check_password('0906'))

        

class LoginTestCase(TestCase):
    def test_login(self):
        
        user = User.objects.create_user(username='developer', password='0000')

        response = self.client.post(
            reverse('users:login_page'),  
            data={
                'username': 'developer',
                'password': '0000'
            }
        )
        self.assertEqual(response.status_code, 302)  
        self.assertTrue(user.is_authenticated)
