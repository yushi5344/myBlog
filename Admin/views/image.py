from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from Admin.models import Cate,Image as mImage
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
import json
import os
from urllib import parse
class Image(View):
    def get(self,request):
        v = request.session.get('is_login', None)
        if not v:
            return redirect('/admin/login')
        # print(request.COOKIES)
        searchName=request.COOKIES.get('searchName',None)
        if not searchName:
            image=mImage.objects.all().values('id','title','thumb','tags','add_time','status','c__name')
        else:
            image=mImage.objects.filter(title=parse.unquote(searchName)).values('id','title','thumb','tags','add_time','status','c__name')
        print(image)
        pagesize = request.COOKIES.get('pagesize', None)
        if not pagesize:
            pagesize=2
        paginator=Paginator(image,pagesize)
        page=request.GET.get('page')
        count=image.count()
        try:
            contacts=paginator.page(page)
        except PageNotAnInteger:
            contacts=paginator.page(1)
        except EmptyPage:
            contacts=paginator.page(paginator.num_pages)
        return render(request,'Admin/image.html',{'image':contacts,'count':count})


def image_add(request):
    if request.method=='GET':
        cate=Cate.objects.filter(p_id=1)
        return render(request,'Admin/image_add.html',{'cate':cate})
    else:
        id=request.POST.get('id',None)
        title = request.POST.get('title', None)
        tags = request.POST.get('tags', None)
        c_id = request.POST.get('c_id', None)
        sort = request.POST.get('sort', None)
        allow_comment = request.POST.get('allow_comment', 0)
        up_time = request.POST.get('up_time', None)
        down_time = request.POST.get('down_time', None)
        contents = request.POST.get('contents', None)
        thumb = request.POST.get('thumb', None)
        if not id:
            try:
                img_url=request.POST.get('img_url',None)
                obj=mImage(
                    title=title,
                    tags=tags,
                    img_url=img_url,
                    allow_comment=allow_comment,
                    status=0,
                    up_time=up_time,
                    down_time=down_time,
                    thumb=thumb,
                    contents=contents,
                    sort=sort,
                    c_id=c_id
                )
                obj.save()
                ret = {'status': True,  'msg': '保存成功'}
            except Exception as e:
                ret = {'status': False, 'msg': '保存失败'}
            return HttpResponse(json.dumps(ret))
        else:
            result=mImage.objects.filter(id=id).update(
                title=title,
                tags=tags,
                allow_comment=allow_comment,
                up_time=up_time,
                down_time=down_time,
                thumb=thumb,
                contents=contents,
                sort=sort,
                c_id=c_id
            )
            ret = {'status': True, 'msg': '修改成功'}
            return HttpResponse(json.dumps(ret))

def upload(request):
    ret={'status':False,'path':None,'msg':None}
    #文件上传
    try:
        obj=request.FILES.get('file')
        file_path=os.path.join('upload',obj.name)
        f=open(file_path,mode='wb')
        for i in obj.chunks():
            f.write(i)
        f.close()
        ret['status']=True
        ret['path']=file_path
        ret['msg']='上传成功'
    except Exception as e:
        ret['status'] = False
        ret['msg'] = '上传失败'
    return HttpResponse(json.dumps(ret))

def image_delete(request,id):
    result=mImage.objects.filter(id=id).delete()
    ret = {'status': True, 'msg': '删除成功'}
    return HttpResponse(json.dumps(ret))

def image_changestate(request,id,status):
    result=mImage.objects.filter(id=id).update(status=status)
    ret = {'status': True, 'msg': '修改成功'}
    return HttpResponse(json.dumps(ret))

def image_edit(request,id):
    cate = Cate.objects.filter(p_id=1)
    image=mImage.objects.filter(id=id).first()
    edit=1
    return render(request,'Admin/image_add.html',{'image':image,'cate':cate,'edit':edit})


def image_show(request,id):
    image=mImage.objects.filter(id=id).first()
    url=image.img_url.split(',')
    length=len(url)
    return render(request,'Admin/image_show.html',{'url':url,'len':length})