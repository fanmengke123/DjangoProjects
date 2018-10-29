from django.shortcuts import render
from .models import *
from django.db.models import Q


# Create your views here.


def index(request):
    banner_list = Banner.objects.all()
    recommand_list = Post.objects.filter(recommend=True).all()[:1]
    post_list = Post.objects.order_by('-pub_date').all()
    category_list = BlogCatrgory.objects.all()
    comment_list = Comment.objects.order_by('-pub_date').all()
    frinedly_link = FriendlyLink.objects.all()

    lists = []
    comments = []
    for comment in comment_list:
        if comment.post_id not in lists:
            comments.append(comment)
            lists.append(comment.post_id)
    ctx = {
        'recommand_list': recommand_list,
        'banner_list': banner_list,
        'post_list': post_list,
        'category_list': category_list,
        'comments': comments[:3],
        'frinedly_link': frinedly_link
    }
    return render(request, 'index.html', ctx)


def search(request):
    if request.method == 'POST':
        kw = request.POST.get('keyword')
        post_list = Post.objects.filter(Q(title__icontains=kw) | Q(content__icontains=kw))

        ctx = {
            'post_list': post_list
        }

    return render(request, 'list.html', ctx)


def blog_list(request):
    post_list = Post.objects.all()
    ctx = {
        'post_list': post_list
    }

    return render(request, 'list.html', ctx)
