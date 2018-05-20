from django.urls import path, re_path
from . import views

app_name= 'webblog'
urlpatterns = [
    path('article-list/', views.article_list, name="articleList"),
    path('getTagsByArticle/<int:article_id>', views.getTagsByArticle, name="getTags"),
    path('like-article/', views.userLike, name="likeArticle"),
    path('read-article/', views.userRead, name="readArticle"),
    path('article-detail/', views.get_article_detail, name="getArticleDetail"),
]