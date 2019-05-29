# -*- coding:utf-8 -*-
# 为应用程序users定义URL模式

from django.urls import path,include,re_path
from . import views


urlpatterns = [
	# 登录页面
	path('',views.login_view, name='login'),
	#注销
	path("logout",views.logout_view,name='logout'),
	# 注册界面
	re_path(r'register/$',views.register,name='register'),
	# test
	path('test',views.test, name='test'),
]
