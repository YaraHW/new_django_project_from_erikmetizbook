"""Определяет схемы URL для пользователей"""
from django.urls import path, include
from . import views

app_name = 'users' # переменной присваивается значение 'users' , чтобы инфраструктура Django могла отличить эти URL-адреса от URL-адресов, принадлежащих другим приложениям
urlpatterns = [
path('', include('django.contrib.auth.urls')), # Включить URL авторизации по умолчанию( набор стандартных хуевин от джанго)
path('register/', views.register, name='register'), # страница регистрации
]