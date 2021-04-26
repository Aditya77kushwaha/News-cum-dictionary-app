from django.urls import path
from . views import index, meaning

urlpatterns = [
    path('', index, name="index"),
    path('mean/', meaning, name="mean")
]
