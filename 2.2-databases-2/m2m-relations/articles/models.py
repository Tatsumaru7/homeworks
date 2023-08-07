# from django.db import models


# class Article(models.Model):

#     title = models.CharField(max_length=256, verbose_name='Название')
#     text = models.TextField(verbose_name='Текст')
#     published_at = models.DateTimeField(verbose_name='Дата публикации')
#     image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
#     tags = models.ManyToManyField('Tag', related_name='scopes', through='Scope', blank=True)

#     class Meta:
#         verbose_name = 'Статья'
#         verbose_name_plural = 'Статьи'
#         ordering = ('-published_at',)

#     def __str__(self):
#         return self.title

# class Tag(models.Model):
#     name = models.CharField(max_length=256, verbose_name='РАЗДЕЛ', default='default') 
#     # article = models.ManyToManyField(Article, related_name='article_tag', through='Scope')
#     def __str__(self):
#         return self.name

# class Scope(models.Model):
#     article = models.ForeignKey(Article, on_delete=models.CASCADE)
#     tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
#     is_main = models.BooleanField( verbose_name='ОСНОВНОЙ')

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    tags = models.ManyToManyField('Tag', through='Scope', blank=True, verbose_name='Теги')
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ('-published_at',)
    
    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название тега', default='default')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        

class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes', verbose_name='Статья')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scopes', verbose_name='Раздел')
    is_main = models.BooleanField(verbose_name='Основной тег')

    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Тематика статьи'
        
