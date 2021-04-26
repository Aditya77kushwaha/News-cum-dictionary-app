from django.urls import path
from . views import index, home

urlpatterns = [
    path('', home, name="home"),
    path('news/', index, name="index")
]
