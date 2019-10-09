from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.a_propos, name="about"),
    path("news/", views.infos, name="news"),
    path("news/details/<int:id>", views.details, name="details"),
    path("news/new_article/", views.new_article, name="new_article"),
    path("news/edit_article/<int:id>",
         views.edit_article, name="edit_article"),
    path("news/delete_article/<int:id>",
         views.delete_article, name="delete_article"),
]
