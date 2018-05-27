# Author guomin
from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from hashlib import sha1
from Admin.models import AdminUser
import json
# Create your views here.
#登录界面
class Login(View):
    def get(self,request):
        v = request.session.get('is_login', None)
        if  v:
            return redirect('/admin/index')
        return render(request,'Admin/login.html')

    def post(self,request):
        ret={'status':False,'msg':None}
        try:
            username=request.POST.get('username')
            pwd=request.POST.get('password')
            online=request.POST.get('online',None)
            psw = sha1()
            psw.update(pwd.encode('utf8'))
            password = psw.hexdigest()
            obj=AdminUser.objects.filter(username=username,password=password).first()
            if obj:
                ret['status']=True
                ret['msg']='登录成功'
                request.session['username']=username
                request.session['is_login']=True
                if online==1:
                    request.session.set_expiry(3600*24*14)
            else:
                ret['status']=False
                ret['msg']='用户名或者密码错误'
        except Exception as e:
            ret['msg']='请求错误'
            ret['status']=False
        rep=HttpResponse(json.dumps(ret))
        return HttpResponse(rep)

def logout(request):
    request.session.clear()
    return redirect('/admin/login')

