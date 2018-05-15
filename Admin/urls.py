# Author guomin
from django.urls import path,re_path
from Admin.views import login
urlpatterns = [
    path('login/',login.Login.as_view()),
]
