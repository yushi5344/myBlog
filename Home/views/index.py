from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from Admin.models import Cate
class Index(View):
    def get(self,request):
        cate=Cate.objects.filter(p_id=3).values('id','name')
        return render(request,'Home/index.html',{'cate':cate})
    def post(self,request):
        pass
    def put(self,request):
        pass
