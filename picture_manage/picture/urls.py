# -*- coding:utf-8 -*-
# 为应用程序users定义URL模式

from django.urls import path,include,re_path
from . import views


urlpatterns = [
	# 主页面
	re_path(r'submit$', views.submit, name='submit'),
	re_path(r'modify$', views.modify, name='modify'),
	re_path(r'add$',views.add,name="add"),
	re_path(r'multiply-(\d+)-(\d+)$',views.multiply,name="multiply"),
	re_path(r'search.html$',views.search,name="search"),
	re_path(r'picture', views.picture, name='picture'),
	re_path(r'delete_(\d+)$', views.delete, name='delete'),
	path('download/<int:a>', views.download, name='download'),
	re_path(r'test$', views.test_image, name='test'),
]
