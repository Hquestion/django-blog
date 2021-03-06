from django.db import models
from markdownx.models import MarkdownxField
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=200)
    order=models.IntegerField(default=0)
    create_time=models.DateTimeField('创建时间', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="类别"


class Tag(models.Model):
    name=models.CharField(max_length=15)
    desc=models.CharField(max_length=200)
    create_time=models.DateTimeField('创建时间', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="标签"


class Article(models.Model):
    YES = 'YES'
    NO = 'NO'
    IS_TOP_CHOICES = (
        ('1', 'YES'),
        ('0', 'NO')
    )
    title=models.CharField("标题", max_length=30)
    poster=models.ImageField("海报图", blank=True, upload_to='uploads/%Y/%m')
    content=MarkdownxField("内容")
    category=models.ForeignKey('Category', on_delete=models.CASCADE, blank=False, verbose_name="类别")
    tag=models.ManyToManyField('Tag', verbose_name="标签")
    create_time=models.DateTimeField('发布日期', auto_now=False)
    update_time=models.DateTimeField('修改日期', auto_now=True)
    is_top=models.CharField("是否置顶",default=NO, choices=IS_TOP_CHOICES, max_length=1)
    is_publish=models.CharField("是否发布", default=YES, choices=IS_TOP_CHOICES, max_length=1)
    is_reprint=models.CharField("是否转载", default=NO, choices=IS_TOP_CHOICES, max_length=1)
    comment_counts=models.IntegerField("评论数量",default=0)
    read_counts=models.IntegerField("阅读数量", default=0)
    fav_counts=models.IntegerField("喜欢数量", default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="文章"
        ordering=("-is_top","-create_time")




class Comment(models.Model):
    user_name=models.CharField(max_length=15, blank=True, default="匿名用户")
    user_email=models.EmailField(blank=True)
    content=models.CharField(max_length=200)
    article=models.ForeignKey('Article', on_delete=models.CASCADE)
    create_time=models.DateTimeField('发表日期', auto_now=True)
    p_comment=models.CharField(max_length=5, blank=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name="评论"
        ordering=("-create_time",)


