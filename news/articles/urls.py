from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="home"),
    path("<slug:url>/", detail_news, name="detail"),
    path('<slug:url>/like/', like, name="like"),
]