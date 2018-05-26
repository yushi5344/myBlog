from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from Admin.models import Cate as mCate,Article
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
class Cate(View):
    def get(self,request,nid):
        article=Article.objects.filter(c_id=nid,status=1).values('id','title','add_time','tags','author')
        pagesize=5
        page=request.GET.get('page')
        paginator=Paginator(article,pagesize)
        try:
            contacts=paginator.page(page)
        except PageNotAnInteger as e:
            contacts=paginator.page(1)
        except EmptyPage as e:
            contacts=paginator.page(Paginator.num_pages)
        cate = mCate.objects.filter(p_id=3).values('id', 'name')
        catename=mCate.objects.filter(id=nid).first()
        return render(request,'Home/cate.html',{'cate':cate,'article':contacts,'catename':catename.name})