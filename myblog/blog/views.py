# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
import json
from blog.serializers import ArticleSerializer
from rest_framework import viewsets, filters
from rest_framework.decorators import api_view




from . import models

def index(request):
	# 返回全部对象，.get(pk=?)获取某个对象
	articles = models.article.objects.all
	return  render(request,'blog/index.html',{'a':articles})

def article(request,article_id):
	print(article_id)
	art = models.article.objects.get(pk=article_id)
	return  render(request,'blog/article_page.html',{'b':art})

def edit_page(request,article_id):
	if str(article_id)=='0':
		return render(request, 'blog/edit_page.html')
	art = models.article.objects.get(pk=article_id)
	return render(request,'blog/edit_page.html',{'c':art})

def edit_submit(request):
	title = request.POST.get('title', 'TITLE')
	content = request.POST.get('content', 'content')
	article_id = request.POST.get('id', 'id')
	if article_id=='0':
	  models.article.objects.create(title=title,content=content)
	  articles = models.article.objects.all
	  return render(request, 'blog/index.html', {'a': articles})
	else:
		a=models.article.objects.get(pk=article_id)
		a.title=title
		a.content=content
		a.save()
		return render(request, 'blog/article_page.html', {'b':a})

@api_view(['GET'])
def test(request):
	articles = models.article.objects.all
	tt = TaskSerializer(articles)
	return Response(tt.data)

@api_view(['GET'])
#queryset设置为Model的queryset，serializer_class设置为刚才定义的serializer。
class BlogViewSet(viewsets.ModelViewSet):
	"""docstring for ClassName"""
	queryset = models.article.objects.all()
	serializer_class = ArticleSerializer

		












