from django.shortcuts import render,HttpResponse
from django.views import View
from Admin.models import Cate,Image as mImage
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
import json
import os
from urllib import parse
class Image(View):
    def get(self,request):
        # print(request.COOKIES)
        searchName=request.COOKIES.get('searchName',None)
        if not searchName:
            image=mImage.objects.all().values('id','title','thumb','tags','add_time','status','c__name')
        else:
            image=mImage.objects.filter(title=parse.unquote(searchName))
        # print(image)
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
        try:
            title=request.POST.get('title',None)
            tags=request.POST.get('tags',None)
            c_id=request.POST.get('c_id',None)
            sort=request.POST.get('sort',None)
            allow_comment=request.POST.get('allow_comment',None)
            up_time=request.POST.get('up_time',None)
            down_time=request.POST.get('down_time',None)
            contents=request.POST.get('contents',None)
            thumb=request.POST.get('thumb',None)
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