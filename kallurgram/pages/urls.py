
from django.urls import path
from .views import LoginView, Register, home, profileView

urlpatterns=[
    path('profileform/',profileView,name='profile-form'),
    path('',home,name='home-page'),
    path('register/',Register,name="register-form"),
    path('login/',LoginView,name="login-page")
]