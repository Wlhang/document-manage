from django.shortcuts import render
from django.http import *
from picture.forms import *
from picture.models import Picture
from django.contrib.auth.decorators import login_required
import os
from django.urls import reverse
import time
from urllib.parse import quote
# Create your views here.

@login_required
def modify(request):
	if request.method == "POST":
		title = request.POST.get("modify_title")
		id = request.POST.get("modify_id")
		Picture.objects.filter(picture_id=id).update(title=title)
		return HttpResponseRedirect("/picture/picture.html")

	
@login_required
def download(request,a):
	download_file = Picture.objects.get(picture_id=int(a))
	download_name = download_file.title
	# print(download_name)
	filename = os.getcwd()+"/picture/media/"+str(request.user.id)+"/img/"+download_name  # 要下载的文件路径
	file = open(filename,'rb')
	if not file:
		return
	response = StreamingHttpResponse(file)
	# response = HttpResponse(file)
	response['Content-Type'] = 'application/octet-stream'
	response['Content-Disposition'] = 'attachment;filename="{0}"'.format(download_name)
	return response


@login_required
def submit(request):
	# upload_file = "./picture/static"
	# if not os.path.exists(upload_file):
	# 	os.mkdir(upload_file)
	# 	pass
	if request.POST:
		form1 = ImageUploadForm(request.POST, request.FILES)
		if form1.is_valid():
			title = request.FILES.get('image').name
			if not os.path.exists(os.getcwd()+"/picture/media/"+str(request.user.id)+"/img/"):
				os.mkdir(os.getcwd()+"/picture/media/"+str(request.user.id))
				os.mkdir(os.getcwd() + "/picture/media/" + str(request.user.id) + "/img")
			if os.path.exists(os.getcwd()+"/picture/media/"+str(request.user.id)+"/img/"+request.FILES.get('image').name):
				title = os.path.splitext(title)[0]+"_"+str(time.strftime('%Y.%m.%d.%H.%M.%S',time.localtime(time.time())))+os.path.splitext(title)[1]
			# new_picture = Picture.objects.create(title=title,picture=form1.cleaned_data['image'],owner=request.user)
			ti = title.split('.')[-1].lower()
			if ti=='bmp' or ti== 'jpg' or ti=='jpge' or ti=='png' or ti=='gif':
				new_picture = Picture.objects.create(title=title,picture='./{}/img/'.format(str(request.user.id))+ title,owner=request.user)
			elif ti=='rm' or ti== 'rmvb' or ti=='mtv' or ti=='avi' or ti=='flv' or ti=='mp4':
				new_picture = Picture.objects.create(title=title,picture='./1.png',owner=request.user)
			else:
				new_picture = Picture.objects.create(title=title,
													 picture='./0.png',
													 owner=request.user)
			new_picture.save()
			doc = open(os.path.join(os.getcwd()+"/picture/media/"+str(request.user.id)+"/img/",title),"wb")
			for chunk in request.FILES.get('image').chunks():
				doc.write(chunk)
			doc.close()
			return HttpResponseRedirect("/picture/picture.html",{"file":"文件上传成功！"})
			pass
		else:
			return HttpResponse("文件后获取失败")
		pass
	else:
		return render(request, "picture/picture.html")
	
@login_required
def search(request):
	if request.method == "POST":
		key = request.POST.get("Search")
		pictures = Picture.objects.filter(title__icontains=key,owner=request.user)
		status = ""
		if len(pictures)<1:
			status="未找到查询结果！"
		context = {
			"pictures": pictures,
			"form1": ImageUploadForm,
			"form2": SearchForm,
			"status":status,
		}
		return render(request,"picture/picture.html",context)
	else:
		return HttpResponseRedirect("/picture/picture.html")
		
	
def add(request):
	num1 = int(request.GET.get("num1"))
	num2 = int(request.GET.get("num2"))
	sum = num1+num2
	context={
		"sum":sum
	}
	return render(request,"picture/test.html",context)


def multiply(request,a,b):
	multiply = int(a)*int(b)
	context={
		"multiply":multiply
	}
	
	#request.session['multiply'] = multiply
	# return HttpResponseRedirect("/picture/test.html",context)
	return render(request,"picture/test.html",context)

@login_required
def picture(request):
	if request.user.is_authenticated:
		pictures = Picture.objects.filter(owner=request.user)
		# pictures = []
		# for picture in pictures1:
		# 	picture.picture = picture.picture[8:]
		# 	pictures.append(picture)
		#
		context = {
			"pictures":pictures,
			"form1":ImageUploadForm,
			"form2":SearchForm,
			"form3":ModifyForm,
		}
		return render(request,"picture/picture.html",context)
	else:
		return HttpResponseRedirect(reverse('user:login'))


def delete(request,a):
	picture = Picture.objects.get(picture_id=a)
	os.remove(os.getcwd()+"/picture/media/"+str(request.user.id)+"/img/"+picture.title)
	picture.delete()
	return HttpResponseRedirect("/picture/picture.html")


def test_image(request):
	picture = Picture.objects.get(picture_id=40)
	return HttpResponse(picture.picture, content_type="image/jpg")
