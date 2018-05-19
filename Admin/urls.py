# Author guomin
from django.urls import path,re_path
from Admin.views import login,index,image,category
urlpatterns = [
    path('login/',login.Login.as_view()),
    path('index/',index.Index.as_view()),
    path('welcome/',index.Welcome.as_view()),
    path('image/',image.Image.as_view()),
    path('category/',category.Category.as_view()),
    path('cate_add/',category.cate_add),
    re_path('cate_edit-(?P<id>\d+)', category.cate_edit),
    re_path('cate_delete-(?P<id>\d+)', category.cate_delete),
]
