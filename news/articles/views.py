from django.shortcuts import render, HttpResponseRedirect
from .models import *

# Create your views here.
def index(request):
    news = Articles.objects.all()
    context = {
        "news": news,
        "title": "Главная страница",

    }

    return render(request, 'articles/base.html', context)


def detail_news(request, url):
    news = Articles.objects.get(slug=url)
    likes = Like.objects.filter(news=news)
    news.views += 1
    news.save()
    context = {
        "news": news,
        "likes": likes,
        "title": "Главная страница",

    }
    return render(request, 'articles/detail.html', context)

def like(request, url):
    news = Articles.objects.get(slug=url)
    likes = Like.objects.filter(user=request.user, news=news)

    if not likes.exists():
        Like.objects.create(user=request.user, news=news)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    else:
        likes.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))