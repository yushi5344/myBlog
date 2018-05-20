from django.shortcuts import render,HttpResponse
from django.views import View
from Admin.models import Cate,Image as mImage
import json
import os
class Image(View):
    def get(self,request):
        return render(request,'Admin/image.html')


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