"""tencent_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import blog.views
import wx.views
import file.views

urlpatterns = [
    path('', blog.views.index),
    path('article/<str:article_id>/', blog.views.show_article),
    path('classification/<str:name>', blog.views.show_article_as_classification),
    path('wx', wx.views.wx),
    path('forbidzh', blog.views.forbid_zhihu),
    path('file/<str:path>', file.views.big_file_download),
    path('admin/', admin.site.urls),
]
