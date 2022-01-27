
from django.urls import path
from .views import LoginView, Register, home, logoutview, profileView

urlpatterns=[
    path('profileform/',profileView,name='profile-form'),
    path('',home,name='home-page'),
    path('register/',Register,name="register-form"),
    path('login/',LoginView,name="login-page"),
    path('logout/',logoutview,name="logout-page")
]