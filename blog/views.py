from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def forbid_zhihu(request):
    return render(request, 'forbidden_zhihu.html')


def index(request):
    articles = Article.objects.all()
    classifications = Classifications.objects.all()
    return render(request, 'article_preview.html',
                  {'navigation': 'nav_classification.html', 'articles': articles,
                   'nav_classifications': classifications})


def show_article(request, article_id):
    article = Article.objects.get(id=article_id)
    classifications = Classifications.objects.all()

    return render(request, 'article.html', {'navigation': 'nav_classification.html',
                                            'article': article, 'nav_classifications': classifications,
                                            'classification_name': '文章分类'})


def show_article_as_classification(request, name):
    classification = Classifications.objects.get(name=name)
    articles = classification.article_set.all()
    return render(request, 'article_preview.html',
                  {'navigation': 'nav_articles.html', 'articles': articles, 'preview': True, 'nav_articles': articles,
                   'classification_name': '全部文章'})
