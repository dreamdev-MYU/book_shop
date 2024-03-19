from django.urls import path
from .views import RegisterView, LoginView
app_name = 'users'
urlpatterns = [
    path('registerpage/', RegisterView.as_view(), name='register'),
    path('loginpage/', LoginView.as_view(), name='loginpage'),
    
]
