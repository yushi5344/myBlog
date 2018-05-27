from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from Admin.models import Cate,Article,Image
class Index(View):
    def get(self,request):
        cate=Cate.objects.filter(p_id=3).values('id','name')
        article=Article.objects.order_by('-add_time')[:3]
        image=Image.objects.filter(status=1).order_by('-add_time')[:7]
        return render(request,'Home/index.html',{'cate':cate,'article':article,'image':image})
    def post(self,request):
        pass
    def put(self,request):
        pass
