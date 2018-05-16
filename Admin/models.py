from django.db import models

# Create your models here.
#后台管理员表
class AdminUser(models.Model):
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=40)
