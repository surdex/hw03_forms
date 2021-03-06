from django.db import models
from django.contrib.auth import get_user_model
from textwrap import shorten

User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="posts")
    group = models.ForeignKey('Group', on_delete=models.SET_NULL,
                              blank=True, null=True, related_name="posts")

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-pub_date']


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return shorten(self.title, width=70, placeholder="...")
