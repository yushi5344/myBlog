# Author guomin
from django.urls import path,re_path
from Admin.views import login,index
urlpatterns = [
    path('login/',login.Login.as_view()),
    path('index/',index.Index.as_view()),
    path('welcome/',index.Welcome.as_view()),
]
