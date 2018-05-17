from django.views import View
from django.shortcuts import render,HttpResponse
from Admin.models import Cate
import json
class Category(View):
    def get(self,request):
        return render(request,'Admin/category.html')

#分类添加
def cate_add(request):
    if request.method=='GET':
        cat=Cate.objects.all().values('id','name')
        return render(request,'Admin/category_add.html',{'cat':cat})
    else:
        ret={'status':False,'msg':None}
        p_id=request.POST.get('p_id')
        name=request.POST.get('name')
        type=request.POST.get('type')
        obj=Cate(
            name=name,
            p_id=p_id,
            type=type
        )
        obj.save()
        ret['status']=True
        ret['msg']='保存成功'
        return HttpResponse(json.dumps(ret))



