from django.db import models

# Create your models here.
#后台管理员表
class AdminUser(models.Model):
    id = models.AutoField(primary_key=True)
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=40)
    login_count=models.BigIntegerField(null=True)
    last_ip=models.GenericIPAddressField(null=True)
    login_time=models.DateTimeField(auto_now_add=True,null=True)

#登录日志
class LoginLog(models.Model):
    id=models.AutoField(primary_key=True)
    u=models.ForeignKey("AdminUser",to_field="id",on_delete=models.CASCADE,null=True)
    login_time=models.DateTimeField(auto_now_add=True)
    login_ip=models.GenericIPAddressField(null=True)


#栏目分类
class Cate(models.Model):
    id=models.AutoField(primary_key=True)
    p_id=models.IntegerField(null=True)
    name=models.CharField(max_length=40)
    type=models.CharField(max_length=40)