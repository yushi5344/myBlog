# Author guomin
from django.urls import path,re_path
from Home.views import index
urlpatterns = [
    path('index/',index.Index.as_view()),
]