from django.shortcuts import render,HttpResponse,redirect
from django.views import View
class Index(View):
    def get(self,request):
        return render(request,'Admin/index.html')
    def post(self,request):
        pass

class Welcome(View):
    def get(self,request):
        return render(request,'Admin/welcome.html')