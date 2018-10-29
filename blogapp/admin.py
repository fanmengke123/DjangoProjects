from django.contrib import admin
from .models import *

# Register your models here.
# 轮播图
admin.site.register(Banner)
# 标签
admin.site.register(Tags)
# 博客文章
admin.site.register(Post)
# 类型
admin.site.register(BlogCatrgory)
# 评论
admin.site.register(Comment)
# 友情链接
admin.site.register(FriendlyLink)
