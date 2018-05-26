from django.shortcuts import render,HttpResponse
from django.views import View
from Admin.models import Article as mArticle,Comment,Cate as mCate
class Article(View):
    def get(self,request,id,nid):
        article=mArticle.objects.filter(id=id).first()
        cate = mCate.objects.filter(p_id=3).values('id', 'name')
        catename = mCate.objects.filter(id=nid).first()
        comment=Comment.objects.filter(a_id=id,status=1).values('content','username','add_time')
        return render(request,'Home/article.html',{'cate':cate,'catename':catename,'article':article,'comment':comment})