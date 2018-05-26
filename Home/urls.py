# Author guomin
from django.urls import path,re_path
from Home.views import index,cate
urlpatterns = [
    path('index/',index.Index.as_view()),
    re_path('cate-(?P<nid>\d+).html', cate.Cate.as_view()),
]