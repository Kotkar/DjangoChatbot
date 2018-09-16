from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'register', views.UserCreate.as_view(), name='registration'),
    url(r'login', views.UserLogin.as_view(), name='login'),
]
