from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=75, verbose_name="Name")
    slug = models.SlugField(verbose_name="URL")

    def __str__(self):
        return self.name

class Articles(models.Model):
    title = models.CharField(max_length=150, verbose_name="title")
    slug = models.SlugField(verbose_name="URL")
    full_text = models.TextField(verbose_name="Full text")
    views = models.PositiveIntegerField(verbose_name="Views")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Category")

    def __str__(self):
        return self.title

class Like(models.Model):
    news = models.ForeignKey(Articles, on_delete=models.CASCADE, verbose_name="News")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
