from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, blank=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    drafted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nom} {self.prenom}"
