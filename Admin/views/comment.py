from django.views import View
from django.shortcuts import render,HttpResponse,redirect
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from Admin.models import Comment as mComment
import json
from urllib import parse
class Comment(View):
    def get(self,request):
        v = request.session.get('is_login', None)
        if not v:
            return redirect('/admin/login')
        searchName=request.COOKIES.get('searchName',None)
        if not searchName:
            comment=mComment.objects.all().values('id','content','username','email','status','add_time','a__title')
        else:
            comment=mComment.objects.filter(a__title=parse.unquote(searchName)).values('id','content','username','email','status','add_time','a__title')
        pagesize=request.COOKIES.get('pagesize')
        if not pagesize:
            pagesize=2
        page=request.GET.get('page',None)
        paginator=Paginator(comment,pagesize)
        count=comment.count()
        try:
            contacts=paginator.page(page)
        except PageNotAnInteger as e:
            contacts=paginator.page(1)
        except EmptyPage as e:
            contacts=paginator.page(Paginator.num_pages)
        return render(request,'Admin/comment.html',{'comment':contacts,'count':count})


def comment_changestate(request,id,status):
    result=mComment.objects.filter(id=id).update(status=status)
    ret={'status':True,'msg':'修改成功'}
    return HttpResponse(json.dumps(ret))

def comment_delete(request,id):
    result=mComment.objects.filter(id=id).delete()
    ret = {'status': True, 'msg': '删除成功'}
    return HttpResponse(json.dumps(ret))

def comment_add(request):
    ret = {'status': False, 'msg': None}
    username= request.POST.get('username', None)
    email = request.POST.get('email', None)
    content = request.POST.get('content', None)
    a_id = request.POST.get('a_id', None)
    try:
        obj = mComment(
            username=username,
            email=email,
            a_id=a_id,
            content=content,
            status=0
        )
        obj.save()
        ret['status'] = True
        ret['msg'] = '评论成功，请等待审核！'
    except Exception as e:
        ret['status'] = False
        ret['msg'] = '评论失败'
    return HttpResponse(json.dumps(ret))