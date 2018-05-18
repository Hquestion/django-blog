from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from django.core import serializers
import json
from markdown import markdown

from .models import Article, Category, Tag
from common.model.models import CommonResponse

# Create your views here.


def article_list(request):
    articles = list(Article.objects.values())[:]

    for index, item in enumerate(articles):
        categoryInfo = model_to_dict(Category.objects.get(pk=item["category_id"]))
        item["categoryInfo"] = {
            "id": categoryInfo['id'],
            "name": categoryInfo['name']
        }
        del(item["category_id"])
        if 'content' in item:
            item["content"] = markdown(item["content"])

    return JsonResponse(CommonResponse(articles).toDict())


def getTagsByArticle(request, article_id):
    article = Article.objects.get(pk=article_id)
    print(article)
    serializers.serialize('json', article)
    return JsonResponse(CommonResponse(serializers.serialize('json', article)).toDict())


def userRead(request, article_id):
    pass

