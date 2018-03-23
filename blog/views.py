from django.shortcuts import render
from markdown import markdown
from .models import *
from django.http import HttpResponseRedirect


def forbid_zhihu(request):
    return render(request, 'forbidden_zhihu.html')


def index_redirect(request):
    return HttpResponseRedirect('http://blog.alphamj.cn/')


def index(request):
    articles = Article.objects.all()
    classifications = Classifications.objects.all()
    return render(request, 'article_preview.html',
                  {'navigation': 'nav_classification.html', 'articles': articles,
                   'nav_classifications': classifications})


def show_article(request, article_id):
    article = Article.objects.get(id=article_id)
    article.content = markdown(article.content, extentions=['markdown.extensions.extra',
                                                            'markdown.extensions.codehilite',
                                                            'markdown.extensions.toc'])
    classifications = Classifications.objects.all()

    return render(request, 'article.html', {'navigation': 'nav_classification.html',
                                            'article': article, 'nav_classifications': classifications,
                                            'classification_name': '文章分类'})


def show_article_as_classification(request, name):
    classification = Classifications.objects.get(name=name)
    articles = classification.article_set.all()
    return render(request, 'article_preview.html',
                  {'navigation': 'nav_articles.html', 'articles': articles, 'nav_articles': articles,
                   'classification_name': '全部文章'})


def post(request):
    if request.method == 'GET':
        classifications = Classifications.objects.all()
        return render(request, 'post.html',
                      {'navigation': 'nav_classification.html', 'classifications': classifications})
    elif request.method == 'POST':
        title = request.POST.get('title')
        context = request.POST.get('context')
        cls = request.POST.getlist('cls')
        if len(title) > 0 and len(context) > 0:
            clss = Classifications.objects.get(name=cls)
        return index(request)

