from django.db import models
from django.contrib.auth.models import User


class Configure(models.Model):
    classifications = models.CharField(max_length=300)


class Classifications(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=300, null=True, blank=True)
    article_number = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now=True)
    classification = models.ManyToManyField(Classifications)

    class Mate:
        get_latest_by = "update_time"
        ordering = "update_time"

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now=True)
    reply_to = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)  # 与自己关联

    def __str__(self):
        return self.article.title + ":" + self.content
