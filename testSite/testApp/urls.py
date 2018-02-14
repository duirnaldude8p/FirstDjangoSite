from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.mainPage, name='mainPage'),
    url(r'^download/$', views.download, name='download'),
    url(r'^account/$', views.account, name='account'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
    url(r'^bussiness/$', views.bussiness, name='bussiness'),
    url(r'^sport/$', views.sport, name='sport'),
    url(r'^create/$', views.create, name='create'),
    url(r'^newsPage/$', views.newsPage, name='newsPage'),
    url(r'^accountInfo/$', views.accountInfo, name='accountInfo'),
]