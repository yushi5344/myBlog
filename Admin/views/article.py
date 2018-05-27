from django.views import View
from django.shortcuts import render,HttpResponse,redirect
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from Admin.models import Cate,Article as mArticle
import json
from urllib import parse
class Article(View):
    def get(self,request):
        v = request.session.get('is_login', None)
        if not v:
            return redirect('/admin/login')
        searchName=request.COOKIES.get('searchName',None)
        if not searchName:
            article=mArticle.objects.all().values('id','title','type','c__name','add_time','source','status')
        else:
            article=mArticle.objects.filter(title=parse.unquote(searchName)).values('id','title','type','c__name','add_time','source','status')
        pagesize=request.COOKIES.get('pagesize',None)
        if not pagesize:
            pagesize=2
        paginator=Paginator(article,pagesize)
        print(pagesize)
        page=request.GET.get('page')
        count=article.count()
        try:
            contacts=paginator.page(page)
        except PageNotAnInteger as e:
            contacts=paginator.page(1)
        except EmptyPage as e:
            contacts=paginator.page(paginator.num_pages)
        return render(request,'Admin/article.html',{'article':contacts,'count':count})


def article_add(request):
    if request.method == 'GET':
        cate = Cate.objects.filter(p_id=3)
        return render(request, 'Admin/article_add.html', {'cate': cate})
    if request.method == 'POST':
        ret = {'status': False, 'msg': None}
        id = request.POST.get('id', None)
        title = request.POST.get('title', None)
        c_id = request.POST.get('c_id', None)
        type = request.POST.get('type', None)
        tags = request.POST.get('tags', None)
        sort = request.POST.get('sort', None)
        describe = request.POST.get('describe', None)
        author = request.POST.get('author', None)
        source = request.POST.get('source', None)
        allow_comment = request.POST.get('allow_comment', 0)
        up_time = request.POST.get('up_time', None)
        down_time = request.POST.get('down_time', None)
        thumb = request.POST.get('thumb', None)
        content = request.POST.get('content', None)
        if not id:
            try:
                obj = mArticle(
                    title=title,
                    c_id=c_id,
                    type=type,
                    tags=tags,
                    sort=sort,
                    describe=describe,
                    author=author,
                    source=source,
                    allow_comment=allow_comment,
                    up_time=up_time,
                    down_time=down_time,
                    thumb=thumb,
                    content=content,
                    status=0
                )
                obj.save()
                ret['status'] = True
                ret['msg'] = '保存成功'
            except Exception as e:
                ret['status'] = False
                ret['msg'] = '保存失败'
        else:
            try:
                result=mArticle.objects.filter(id=id).update(
                    title=title,
                    c_id=c_id,
                    type=type,
                    tags=tags,
                    sort=sort,
                    describe=describe,
                    author=author,
                    source=source,
                    allow_comment=allow_comment,
                    up_time=up_time,
                    down_time=down_time,
                    thumb=thumb,
                    content=content,
                    status=0
                )
                ret['status'] = True
                ret['msg'] = '修改成功'
            except Exception as e:
                ret['status'] = False
                ret['msg'] = '修改失败'
        return HttpResponse(json.dumps(ret))


def article_changestate(request,id,status):
    result = mArticle.objects.filter(id=id).update(status=status)
    ret = {'status': True, 'msg': '修改成功'}
    return HttpResponse(json.dumps(ret))

def article_delete(request,id):
    result=mArticle.objects.filter(id=id).delete()
    ret={'status':True,'msg':'修改成功'}
    return HttpResponse(json.dumps(ret))

def article_edit(request,id):
    cate = Cate.objects.filter(p_id=3)
    article=mArticle.objects.filter(id=id).first()
    return render(request, 'Admin/article_add.html', {'cate': cate,'article':article})
