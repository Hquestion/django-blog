from django.urls import path
from . import views

urlpatterns = [
    path('/article-list/', views.article_list, name="articleList")
]