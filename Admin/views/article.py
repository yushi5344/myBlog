from django.views import View
from django.shortcuts import render,HttpResponse
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

class Article(View):
    def get(self,request):
        return render(request,'Admin/article.html')