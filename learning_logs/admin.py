from django.contrib import admin

# Тут мы регаем созданные модели в models.py чтоб они отображались на самом сайте в панели админки
# Моя модель

from .models import Topic, Entry  # точка перед моделс означает что модель следует искать в одном каталоге с admin.py
admin.site.register(Topic)
admin.site.register(Entry)