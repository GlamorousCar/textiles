from .views import index
from django.urls import path
from .views import *
from django.urls import path, include
from . import views

urlpatterns = [
    path('', index),
    path('category/<slug:slug>', category_view, name='category_detail'),
    path('category/<str:name>/<slug:slug>', item_view, name='item-detail'),
]