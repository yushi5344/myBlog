from django.views import View
from django.shortcuts import render,HttpResponse
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from Admin.models import Cate
import json
class Category(View):
    def get(self,request):
        cat=Cate.objects.all()
        pagesize=2
        if not pagesize:
            pagesize=1
        paginator=Paginator(cat,pagesize)
        page=request.GET.get('page')
        try:
            contacts=paginator.page(page)
        except PageNotAnInteger:
            contacts=paginator.page(1)
        except EmptyPage:
            contacts=paginator.page(paginator.num_pages)
        print(contacts)
        return render(request,'Admin/category.html',{'cate':contacts})

#分类添加
def cate_add(request):
    if request.method=='GET':
        cat=Cate.objects.all().values('id','name','level')
        return render(request,'Admin/category_add.html',{'cat':cat})
    else:
        ret={'status':False,'msg':None}
        p_id=request.POST.get('p_id')
        name=request.POST.get('name')
        type=request.POST.get('type')
        cate=Cate.objects.filter(id=p_id).first()
        obj=Cate(
            name=name,
            p_id=p_id,
            type=type,
            level=cate.level+1
        )
        obj.save()
        ret['status']=True
        ret['msg']='保存成功'
        return HttpResponse(json.dumps(ret))



