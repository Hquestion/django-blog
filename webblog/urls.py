from django.urls import path, re_path
from . import views

app_name= 'webblog'
urlpatterns = [
    path('article-list/', views.article_list, name="articleList"),
    path('getTagsByArticle/', views.getTagsByArticle, name="getTags"),
    path('like-article/', views.userLike, name="likeArticle"),
    path('read-article/', views.userRead, name="readArticle"),
    path('article-detail/', views.get_article_detail, name="getArticleDetail"),
    path('article-comment/', views.article_comment_list, name="getArticleComment"),
    path('comment/', views.comment, name="ArticleComment")
]