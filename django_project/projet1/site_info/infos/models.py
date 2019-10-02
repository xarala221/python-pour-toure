from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    titre = models.CharField(max_length=150)
    contenu = models.TextField()
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_publication = models.DateTimeField(
        auto_now_add=False, blank=True, null=True)
    date_modification = models.DateTimeField(
        auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return self.titre
