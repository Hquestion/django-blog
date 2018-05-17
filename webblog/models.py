from django.db import models
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=200)
    order=models.IntegerField(default=0)
    create_time=models.DateTimeField('创建时间', auto_now=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name=models.CharField(max_length=15)
    desc=models.CharField(max_length=200)
    create_time=models.DateTimeField('创建时间', auto_now=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    YES = 'YES'
    NO = 'NO'
    IS_TOP_CHOICES = (
        (1, 'YES'),
        (0, 'NO')
    )
    title=models.CharField("标题", max_length=30)
    poster=models.ImageField("海报图", blank=True, upload_to='uploads/%Y/%m')
    content=models.TextField("内容")
    category=models.ForeignKey('Category', on_delete=models.CASCADE, blank=False, verbose_name="类别")
    tag=models.ManyToManyField('Tag', verbose_name="标签")
    create_time=models.DateTimeField('发布日期', auto_now=True)
    update_time=models.DateTimeField('修改日期', auto_now=True)
    is_top=models.IntegerField("是否置顶",default=NO, choices=IS_TOP_CHOICES)
    is_publish=models.IntegerField("是否发布", default=YES, choices=IS_TOP_CHOICES)
    is_reprint=models.IntegerField("是否转载", default=NO, choices=IS_TOP_CHOICES)
    comment_counts=models.IntegerField("评论数量",default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="文章"




class Comment(models.Model):
    user_name=models.CharField(max_length=15, blank=True)
    user_email=models.EmailField(blank=True)
    content=models.CharField(max_length=200)
    article=models.ForeignKey('Article', on_delete=models.CASCADE)
    create_time=models.DateTimeField('发表日期', auto_now=True)
    p_comment=models.ForeignKey('Comment', on_delete=models.CASCADE)

    def __str__(self):
        return self.content


