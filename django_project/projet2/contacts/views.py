from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact

# Create your views here.


def index(request):
    return render(request, "pages/index.html")

def about(request):
    return render(request, "pages/about.html")

# afficher la liste des contacts
@login_required(login_url="/login/")
def liste_des_contacts(request):
    user = request.user
    contacts = Contact.objects.filter(auteur=user).order_by("-id")
    contacts = contacts.filter(drafted=False)
    context = {"contacts": contacts}
    return render(request, "contacts/contact_list.html", context)

# le detail du contact
@login_required(login_url="/login/")
def details_contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    context = {"contact": contact}
    return render(request, "contacts/details_contact.html", context)

# creer nouveau contact


def nouveau_contact(request):
    if request.method == "POST":
        auteur = request.user
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        contact = Contact.objects.create(
            nom=nom,
            prenom=prenom,
            phone=phone,
            email=email,
            auteur=auteur
        )
        contact.save()
        return redirect("/contacts/")

    return render(request, "contacts/nouveau_contact.html")


# modifier un contact
def modifier_contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == "POST":
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        Contact.objects.filter(pk=contact.id).update(
            nom=nom,
            prenom=prenom,
            phone=phone,
            email=email
        )
        return redirect("/contacts/")
    context = {"contact": contact}
    return render(request, "contacts/modifier_contact.html", context)

# supprimer un contact
@login_required(login_url="/login/")
def supprimer_contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == "POST":
        # contact.delete()
        Contact.objects.filter(pk=contact.id).update(
            drafted=True
        )
        return redirect("/contacts/")
    context = {"contact": contact}
    return render(request, "contacts/supprimer_contact.html", context)
