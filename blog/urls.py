from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^article/(?P<id>\d+)', views.show_article),
    url(r'^classification/(?P<name>.+)', views.show_article_as_classification),
    url(r'^', views.index)
]