from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.a_propos, name="about"),
    path("news/", views.infos, name="news"),
    path("news/details/<int:id>", views.details, name="details"),
]
