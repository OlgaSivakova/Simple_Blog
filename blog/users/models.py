from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime  


# Create your models here.
class PostQuerrySet(models.QuerySet):
    def titles(self):
        return self.order_by('-dats')

class Post(models.Model):
    title = models.CharField('Заголовок записи', max_length=100)
    descript = models.TextField('Текст блога')
    author = models.CharField('Имя автора', max_length=100)
    dats = models.DateTimeField(default=datetime.now())
    
    img = models.ImageField('Изображение', upload_to = 'image/%Y')# c указанием текущего года, это путь где будут храниться все излбражения с админки
    
    objects =  PostQuerrySet.as_manager()
    
    def __str__(self):
        return f'{self.title}, {self.author}' #отображение в списке всех записей в админке
    
    
    class Meta:
        verbose_name = 'Запись' #красивое отображение  в админке
        verbose_name_plural = 'Записи'
        

class Comments(models.Model):
    name = models.CharField('Имя автора', max_length=100)
    textcom = models.TextField('Комментарий', max_length=2000)
    post = models.ForeignKey(Post, verbose_name="Публикация",on_delete=models.CASCADE, related_name='compos') #связь с моделью публикацийь при удалении - каскад - удаляется и комментарий к публикации
    
    def __str__(self):
        return f'{self.name}, {self.post}' #отображение в списке всех записей в админке
    
    class Meta:
        verbose_name = 'Комментарий' #красивое отображение  в админке
        verbose_name_plural = 'Комментарии'


class User(AbstractUser):
    pass

class Likes(models.Model):
    ip = models.CharField('IP-адрес', max_length=100)
    pos = models.ForeignKey(Post, verbose_name='Понравившееся', on_delete=models.CASCADE)
    
    
    
class Dressingroom(models.Model):
    num = models.CharField('Номсер гримёрки', max_length=100)
    
    def __str__(self):
        return f'{self.num}'
    
class Director(models.Model):
    dirname = models.CharField('Имя режисёра', max_length=100)
    
    def __str__(self):
        return f'{self.dirname}'
    
class Movie(models.Model):
    title = models.CharField('Имя актёра', max_length=100)
    direc = models.ForeignKey(Director,on_delete=models.CASCADE, null = True, blank=True, related_name='moviess')

    def __str__(self):
        return f'{self.title}, {self.direc}'
    
class Actor(models.Model):
    name = models.CharField('Имя актёра', max_length=100)
    dress = models.OneToOneField(Dressingroom, on_delete=models.CASCADE, null = True, blank=True)
    mov = models.ManyToManyField(Movie, related_name='connect')
    
    def __str__(self):
        return f'{self.name}, {self.dress}'
    
