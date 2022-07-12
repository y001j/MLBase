from django.template.defaulttags import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_picture',views.get_picture, name='getpicture')   # 获取图片
]
