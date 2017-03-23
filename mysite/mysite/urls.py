"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from polls import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls', namespace="polls")),  # 在这里增加了命名空间
    url(r'^address/', include('polls.urls')),  # 上传学生名单的url
    url(r'^$', include('polls.urls')),
    url(r'^GetClassData/$', views.Return_Class_Data),  # 联动下拉菜单获取班级的url
]
# 这里相当于是连接的根引导！ 从这里看是进行正则判断