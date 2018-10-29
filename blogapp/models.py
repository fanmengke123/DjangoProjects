from django.db import models
from userapp.models import BlogUser
from datetime import datetime


# Create your models here.
# 轮播图
class Banner(models.Model):
    title = models.CharField(verbose_name='标题', max_length=20)
    cover = models.ImageField(verbose_name='轮播图', upload_to='static/images/banner')
    link_url = models.URLField(verbose_name='图片链接', max_length=128)
    idx = models.IntegerField(verbose_name='索引')
    is_active = models.BooleanField(verbose_name='是否是active', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name


# 博客分类
class BlogCatrgory(models.Model):
    name = models.CharField(verbose_name='分类名称', max_length=20, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name


# 标签模型
class Tags(models.Model):
    name = models.CharField(verbose_name='标签名称', max_length=20, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name


# 博客模型
class Post(models.Model):
    user = models.ForeignKey(BlogUser, verbose_name='作者')
    category = models.ForeignKey(BlogCatrgory, verbose_name='博客分类')
    tags = models.ManyToManyField(Tags, verbose_name='标签')
    title = models.CharField('标题', max_length=50)
    content = models.TextField('内容')
    pub_date = models.DateTimeField('发布日期', default=datetime.now)
    cover = models.ImageField('博客封面', upload_to='static/images/post', default=None)
    views = models.IntegerField('浏览数', default=0)
    recommend = models.BooleanField('推荐博客', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '博客'
        verbose_name_plural = verbose_name


# 评论类
class Comment(models.Model):
    post = models.ForeignKey(Post, verbose_name='博客')
    user = models.ForeignKey(BlogUser, verbose_name='作者')
    pub_date = models.DateTimeField('发布时间')
    content = models.TextField('内容')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'


# 友情链接类
class FriendlyLink(models.Model):
    title = models.CharField('标题', max_length=50)
    link = models.URLField('链接', max_length=50, default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = '友情链接'
