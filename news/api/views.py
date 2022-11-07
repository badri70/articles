from django.urls import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import AbstractUser
from articles.models import Articles
from .serializers import ArticlesSerializers
from django.shortcuts import HttpResponseRedirect
# Create your views here.

@api_view(['GET'])
def articles_list(request):
    user = request.user
    if user.is_staff:
        articles = Articles.objects.all()
        serializer = ArticlesSerializers(articles, many=True)
        return Response(serializer.data)
    else:
        return HttpResponseRedirect(reverse('home'))