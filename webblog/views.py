from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F
from django.core import serializers
import json
from markdown import markdown

from .models import Article, Category, Tag
from common.model.models import CommonResponse

# Create your views here.


def article_list(request):
    articles = list(Article.objects.values())[:]

    for index, item in enumerate(articles):
        # 获取类别信息
        categoryInfo = model_to_dict(Category.objects.get(pk=item["category_id"]))
        item["categoryInfo"] = {
            "id": categoryInfo['id'],
            "name": categoryInfo['name']
        }
        del(item["category_id"])
        # 获取标签信息
        article = model_to_dict(Article.objects.get(pk=item["id"]))
        tagList = []
        for i, tagItem in enumerate(list(article["tag"])):
            tag = model_to_dict(tagItem)
            tagList.append(tag)
        item["tag"] = tagList
        # 转化markdown
        if 'content' in item:
            item["content"] = markdown(item["content"])

    return JsonResponse(CommonResponse(articles).toDict())


def getTagsByArticle(request):
    article = model_to_dict(Article.objects.get(pk=request.GET["article_id"]))
    tagList = []
    for i, item in enumerate(list(article["tag"])):
        tag = model_to_dict(item)
        tagList.append(tag)
    return JsonResponse(CommonResponse(tagList).toDict())


def get_article_detail(request):
    article = model_to_dict(Article.objects.get(pk=request.GET["id"]))
    article["poster"] = str(article["poster"])
    print(article)
    categoryInfo = model_to_dict(Category.objects.get(pk=article["category"]))
    article["categoryInfo"] = {
        "id": categoryInfo['id'],
        "name": categoryInfo['name']
    }
    del (article["category"])
    # 获取标签信息
    tagList = []
    for i, tagItem in enumerate(list(article["tag"])):
        tag = model_to_dict(tagItem)
        tagList.append(tag)
        article["tag"] = tagList
    # 转化markdown
    if 'content' in article:
        article["content"] = markdown(article["content"])
    return JsonResponse(CommonResponse(article).toDict())


@csrf_exempt
def userRead(request):
    data = json.loads(request.body.decode())
    article = Article.objects.get(pk=data["id"])
    article.read_counts = F('read_counts') + 1
    article.save()
    count = Article.objects.get(pk=data["id"]).read_counts
    return JsonResponse(CommonResponse(count).toDict())


@csrf_exempt
def userLike(request):
    data = json.loads(request.body.decode())
    article = Article.objects.get(pk=data["id"])
    count = F('fav_counts') + 1
    article.fav_counts = count
    article.save()
    count = Article.objects.get(pk=data["id"]).fav_counts
    return JsonResponse(CommonResponse(count).toDict())

