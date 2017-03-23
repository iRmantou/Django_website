from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', views.detail, name='detail'),
    url(r'^vote1/$', views.vote1, name='vote1'), #view参数指定视图函数！ name是命名这个url，后面再其他地方就可以通过这个名字来明确的引用
    url(r'^vote2/$', views.vote2, name='vote2'),
    url(r'^vote3/$', views.vote3, name='vote3'),
    url(r'^vote4/$', views.vote4, name='vote4'),
    url(r'^upload/', views.upload, name="upload"),
    url(r'^questionclassdata/', views.questionclassdata, name="questionclassdata"),
    url(r'^getResult/', views.getResult, name="getResult"),
    url(r'^$', views.login, name='login'),

]
