
from django.urls import path
from .views import home, profileView

urlpatterns=[
    path('profileform/',profileView,name='profile-form'),
    path('',home,name='home-page')
]