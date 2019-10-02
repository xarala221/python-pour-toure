from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article


def index(request):
    return render(request, "index.html")


def a_propos(request):
    return render(request, "about.html")


def infos(request):
    articles = Article.objects.all()
    context = {"articles": articles}
    return render(request, "infos/news.html", context)


def details(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, "infos/details.html", {"article": article})
