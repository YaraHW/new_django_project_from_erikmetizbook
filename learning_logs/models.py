from django.db import models # по сути это путь для импорта папки models(приложения) django и db это тоже папки(приложения)
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model): # models - папка, Model - класс, находится в base.py папки model
    """Тема, которую изучает пользователь"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True) #auto_add_now=True приказывает Django автоматически присвоить этому
                                                    # атрибуту текущую дату и время каждый раз, когда пользователь создает новую тему.
    owner = models.ForeignKey(User, on_delete=models.CASCADE) # для связывания конкретных данных(тем, топиков) с конкр. пользователем, если пользователь удалится то и данные тоже
    def __str__(self):                               # __str__ для возврата текста в строчке а не в хуете типо 0х0003213
        """Возвращает строковое представление модели."""
        return self.text


class Entry(models.Model):
    """Информация, изученная пользователем по теме"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)  #Foreign Key - внешний ключ содержит ссылку на другую запись в базе данных. Таким образом каждая запись связывается с конкретной темой
    #Аргумент on_delete=models.CASCADE сообщает Django, что при удалении темы все записи, связанные с этой темой, также должны быть удалены (это называется каскадным удалением).
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)  # Атрибут date_added позволяет отображать записи в порядке их создания и снабжать каждую запись временной меткой.
    class Meta:
        verbose_name_plural = 'entries'  # это просто чтоб он множественное число брал как entries а не entrys(ибо неправильно)

    """Возвращает строковое представление модели."""
    def __str__(self):
        if len(self.text) > 50:
            return (f"{self.text[:50]}...")
        else:
            return (f"{self.text[:50]}")

