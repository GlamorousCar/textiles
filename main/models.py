from django.db import models
import string
import random

from django.utils.text import slugify
# Create your models here.
from django.db import models
from django.urls import reverse
"""У нас есть модели: Товар, Корзина, Элемент Корзины, Пользователь.
Модель Корзина привязана к модели Пользователь (через foreign key).
Модель Элемент Корзины также привязана к модели Пользователь (через foreign key).
Модель Товар также привязана к модели Элемент Корзины (через foreign key).
В модели Корзина есть поле m2m для элементов корзины.
"""
def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'

    @property
    def get_products(self):
        return Product.objects.filter(category__name=self.name)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.name)
        super(Category, self).save(*args, **kwargs)



class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    availability = models.BooleanField(default=True, verbose_name='В наличии')
    size = models.JSONField()
    description = models.TextField(default='Описание',verbose_name='Описание', null=True)
    image = models.ImageField(verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='Время изменения')
    quantity = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.title)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_model_name(self):
        return self.__class__.__name__.lower()

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'

    def get_absolute_url(self):
        return f'/category/{self.category}'+'/'+f'{self.slug}'


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    def __str__(self):
        return self.image.name