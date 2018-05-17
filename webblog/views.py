from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json

from .models import Article

# Create your views here.


def article_list(request):
    articles = Article.objects.values('id', 'title', 'content', 'category__name', 'tag__name')
    print(list(articles))
    result = list(articles)[:]
    print(result)

    return JsonResponse({'code': 200, 'data': result})