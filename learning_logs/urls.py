"""Определяет схемы URL для learning_logs."""

from django.urls import path #path  необходима для связывания URL с представлениями(c views)

from . import views #точка приказывает Python импортировать представления из каталога, в котором находится текущий модуль urls.py .т.е из (views.py)

app_name = 'learning_logs' #app_name помогает Django отличить этот файл urls.py от одноименных файлов в других приложениях в проекте
# Домашняя страница

urlpatterns = [    #urlpatterns в этом модуле представляет собой список страниц, которые могут запрашиваться из приложения learning_logs

# """Определяет схемы URL для learning_logs."""
path('', views.index, name='index'),

path('topics/', views.topics, name='topics'), # Страница со списком всех тем.
path('topics/<int:topic_id>/', views.topic, name='topic'), # Страница с подробной информацией по отдельной теме
path('new_topic/', views.new_topic, name='new_topic'),  # страница добавления новой темы
path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'), # Страница для добавления новой записи
path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'), # Страница для редактирования записи
]