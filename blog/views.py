from django.shortcuts import render
from . import models
# Create your views here.
from django.http import HttpResponse

def index(request):
    #return HttpResponse('hello，world')
    articles = models.Article.objects.all()
    return render(request,'blog/index.html',{'articles':articles})


def article_page(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request,'blog/article_page.html',{'article':article})

def edit_page(request,):
    return render(request,'blog/edit_page.html')


def edit_action(request):
    title = request.POST.get('title','default TITLE')
    content = request.POST.get('content','default CONTENT')
    models.Article.objects.create(title=title,content=content)
    articles = models.Article.objects.all()
    return render(request,'blog/index.html',{'articles':articles})

def update_article(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request,'blog/update_article.html',{'article':article})


def update_action(request,article_id):
    title = request.POST.get('title','default TITLE')
    content = request.POST.get('content','default CONTENT')
    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    articles = models.Article.objects.all()
    return render(request,'blog/index.html',{'articles':articles})
