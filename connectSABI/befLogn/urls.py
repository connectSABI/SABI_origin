from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='registerPage'),
    path('formCheck', views.formCheck, name='TestForm')
]
