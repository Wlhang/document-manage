from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Picture(models.Model):
	picture_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=20)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	def user_directory_path(instance, filename):
		return './{}/img/'.format(str(instance.owner.id))+ instance.title
	# picture = models.FileField(upload_to=user_directory_path)
	picture = models.CharField(max_length=50)
	
	def __str__(self):
		# 返回模型的字符串表示
		return self.title