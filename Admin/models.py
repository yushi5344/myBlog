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
    level=models.IntegerField(null=True)

#图片
class Image(models.Model):
    id=models.AutoField(primary_key=True)
    c=models.ForeignKey('Cate',to_field='id',on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=40)
    tags=models.CharField(max_length=255)
    img_url=models.TextField(null=True)
    allow_comment=models.BooleanField(blank=True)
    add_time = models.DateTimeField(auto_now_add=True, null=True)
    status=models.IntegerField(default=0)
    up_time=models.DateTimeField(null=True)
    down_time=models.DateTimeField(null=True)
    thumb=models.TextField(null=True)
    contents=models.CharField(max_length=255)
    sort=models.IntegerField(default=1)

#文章
class Article(models.Model):
    id=models.AutoField(primary_key=True)
    c = models.ForeignKey('Cate', to_field='id', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=40)
    tags = models.CharField(max_length=255)
    allow_comment = models.BooleanField(blank=True)
    add_time = models.DateTimeField(auto_now_add=True, null=True)
    status = models.IntegerField(default=0)
    up_time = models.DateTimeField(null=True)
    down_time = models.DateTimeField(null=True)
    thumb = models.TextField(null=True)
    describe = models.CharField(max_length=255)
    sort = models.IntegerField(default=1)
    author=models.CharField(max_length=50)
    source=models.CharField(max_length=50)
    type=models.IntegerField(null=True)
    content = models.TextField(null=True)

