from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json
from markdown import markdown

from .models import Article, Category, Tag
from common.model.models import CommonResponse

# Create your views here.


def article_list(request):
    articles = Article.objects.values()
    result = list(articles)[:]

    for index, item in enumerate(result):
        if 'content' in item:
            item["content"] = markdown(item["content"])

    return JsonResponse(CommonResponse(result).toDict())