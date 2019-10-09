from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    titre = forms.CharField(label="Titre", max_length=150)
    contenu = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Article
        fields = ('titre', 'contenu',)
