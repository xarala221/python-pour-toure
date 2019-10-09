from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Article
from .forms import ArticleForm


def index(request):
    return render(request, "index.html")


def a_propos(request):
    return render(request, "about.html")


def infos(request):
    articles = Article.objects.order_by('-id')
    context = {"articles": articles}
    return render(request, "infos/news.html", context)


def details(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, "infos/details.html", {"article": article})


def new_article(request):
    user = request.user
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            titre = form.cleaned_data['titre']
            contenu = form.cleaned_data['contenu']
            article = Article.objects.create(
                titre=titre,
                contenu=contenu,
                auteur=user
            )
            article.save()
            return redirect("/news/")
    else:
        form = ArticleForm()

    return render(request, "infos/new_article.html", {"form": form})


def edit_article(request, id):
    article = get_object_or_404(Article, id=id)
    user = request.user
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            titre = form.cleaned_data['titre']
            contenu = form.cleaned_data['contenu']
            Article.objects.filter(id=article.id).update(
                titre=titre,
                contenu=contenu,
                auteur=user
            )
            article.save()
            return redirect(f"/news/details/{article.id}")
    else:
        form = ArticleForm(instance=article)

    return render(request, "infos/edit_article.html", {"form": form})


def delete_article(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == "POST":
        article.delete()
        return redirect("/news/")
    else:
        message = "Confirmez la suppression ?"
    return render(request, "infos/delete.html", {"message": message, "article": article})
