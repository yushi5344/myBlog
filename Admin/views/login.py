# Author guomin
from django.shortcuts import render,HttpResponse
from django.views import View
# Create your views here.
#登录界面
class Login(View):
    def get(self,request):
        return render(request,'Admin/login.html')

    def post(self,request):
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username)
        print(password)
        return HttpResponse('哈哈哈')