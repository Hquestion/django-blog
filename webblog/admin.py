from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Category, Tag, Article, Comment

# Register your models here.

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Article, MarkdownxModelAdmin)
