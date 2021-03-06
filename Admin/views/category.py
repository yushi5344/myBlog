from django.views import View
from django.shortcuts import render,HttpResponse,redirect
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from Admin.models import Cate
import json
from urllib import parse
class Category(View):
    def get(self,request):
        v = request.session.get('is_login', None)
        if not v:
            return redirect('/admin/login')
        searchName=request.COOKIES.get('searchName',None)
        if not searchName:
            cat = Cate.objects.all()
        else:
            p = parse.unquote(searchName)
            cat=Cate.objects.filter(name=p)
        pagesize = request.COOKIES.get('pagesize', None)
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
        return render(request,'Admin/category.html',{'cate':contacts})

#分类添加
def cate_add(request):
    if request.method=='GET':
        cat=Cate.objects.all().values('id','name','level')
        return render(request,'Admin/category_add.html',{'cat':cat})
    else:
        ret={'status':False,'msg':None}
        id=request.POST.get('id',None)
        if not id:
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
        else:
            p_id = request.POST.get('p_id')
            name = request.POST.get('name')
            type = request.POST.get('type')
            result=Cate.objects.filter(id=id).update(
                p_id=p_id,
                name=name,
                type=type
            )
            ret['status'] = True
            ret['msg'] = '修改成功'
        return HttpResponse(json.dumps(ret))

def cate_edit(request,id):
    obj=Cate.objects.filter(id=id).first()
    cat = Cate.objects.all().values('id', 'name', 'level')
    return  render(request,'Admin/category_add.html',{'cate':obj,'cat':cat})

def cate_delete(request,id):
    result=Cate.objects.filter(id=id).delete()
    ret = {'status': True, 'msg': '删除成功'}
    return HttpResponse(json.dumps(ret))

