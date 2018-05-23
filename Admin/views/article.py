from django.views import View
from django.shortcuts import render,HttpResponse
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from Admin.models import Cate,Article as mArticle
import json
class Article(View):
    def get(self,request):
        return render(request,'Admin/article.html')


def article_add(request):
    if request.method == 'GET':
        cate = Cate.objects.filter(p_id=3)
        return render(request, 'Admin/article_add.html', {'cate': cate})
    if request.method == 'POST':
        ret = {'status': False, 'msg': None}
        print(request.POST)
        title = request.POST.get('title', None)
        c_id = request.POST.get('c_id', None)
        type = request.POST.get('type', None)
        tags = request.POST.get('tags', None)
        sort = request.POST.get('sort', None)
        describe = request.POST.get('describe', None)
        author = request.POST.get('author', None)
        source = request.POST.get('source', None)
        allow_comment = request.POST.get('allow_comment', None)
        up_time = request.POST.get('up_time', None)
        down_time = request.POST.get('down_time', None)
        thumb = request.POST.get('thumb', None)
        content = request.POST.get('content', None)
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
        return HttpResponse(json.dumps(ret))
