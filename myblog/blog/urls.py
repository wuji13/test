from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^article/(?P<article_id>[0-9]+)', views.article,name='article_page'),
    url(r'^edit/(?P<article_id>[0-9]+)', views.edit_page,name='edit_page'),
    url(r'^edit/action', views.edit_submit,name='article_action'),
    url(r'^test',views.test),
   	url(r'^blog',views.BlogViewSet), 
]