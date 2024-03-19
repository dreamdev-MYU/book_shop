
from django.contrib import admin
from django.urls import path, include
from .views import landingpage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landingpage, name='landingpage'),
    path('users/', include('users.urls')),
]
