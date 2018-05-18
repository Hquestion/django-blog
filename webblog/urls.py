from django.urls import path, re_path
from . import views

app_name= 'webblog'
urlpatterns = [
    path('article-list/', views.article_list, name="articleList")
]