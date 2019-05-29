from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from user.forms import LoginForm


# Create your views here.

# 登陆账户
def login_view(request):
	if request.method == "POST":
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			cd = login_form.cleaned_data
			user = authenticate(username=cd['username'], password=cd['password'])
			if user:
				# request.session["info"] = "infomation"
				'''用户登陆后，Django会自动调用默认的session应用，
					将用户的id存至session中，通常情况下，login与authenticate
					配合使用'''
				login(request, user)
				# request.session.set_expiry(0)  # 关闭浏览器自动退出登录
				return HttpResponseRedirect(reverse('picture:picture'))
			else:
				return render(request, 'user/login.html',
							  {"form": login_form, 'status': 'ERROR Incorrect username or password'})
		else:
			return render(request, 'user/login.html', {"form": login_form, 'status': '输入不合法'})
	elif request.method == "GET":
		if request.user.is_authenticated:
			return HttpResponseRedirect(reverse('picture:picture'))
		else:
			login_form = LoginForm()
			return render(request, 'user/login.html', {"form": login_form})
	
# 注销账户
def logout_view(request):
	request.session.clear()
	logout(request)
	return HttpResponseRedirect(reverse('user:login'))


def register(request):
	# 注册新用户
	if request.method != 'POST':
		# 显示空的注册表
		form = UserCreationForm()
	else:
		# 处理填写好的表单
		form = UserCreationForm(data=request.POST)
		
		if form.is_valid():
			new_user = form.save()
			# 让用户自动登录，再重定向到主页
			authenticate_user = authenticate(username=new_user.username, password=request.POST['password1'])
			login(request, authenticate_user)
			return HttpResponseRedirect(reverse('picture:picture'))
	
	context = {'form': form}
	return render(request, 'user/register.html', context)

def test(request):
	context = {
		"info":request.session.get("info")
	}
	return render(request,"user/test.html",context)