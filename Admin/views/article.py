from django.views import View
from django.shortcuts import render,HttpResponse
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

class Article(View):
    def get(self,request):
        return render(request,'Admin/article.html')

def article_add(request):
    if request.method=='GET':
        return render(request,'Admin/article_add.html')