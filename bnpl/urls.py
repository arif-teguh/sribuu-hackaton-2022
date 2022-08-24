from django.urls import path

from .views import index

urlpatterns = [
    path(
        "",
        index,
        name="index",
    ),
    path(
        "haha",
        index,
        name="index2",
    ),
]
