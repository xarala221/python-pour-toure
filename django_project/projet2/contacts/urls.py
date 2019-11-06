from django.urls import path, include
from rest_framework import routers
from . import views
from . import api
router = routers.DefaultRouter()
router.register("api/contacts", api.ContactViewSet, basename="contacts")

urlpatterns = [
    path("", views.index, name="index"),
    path("contacts/", views.liste_des_contacts, name="contacts"),
    path("contacts/<int:id>/", views.details_contact, name="details"),
    path("contacts/nouveau/", views.nouveau_contact, name="nouveau"),
    path("contacts/<int:id>/modifier/", views.modifier_contact, name="modifier"),
    path("contacts/<int:id>/supprimer/",
         views.supprimer_contact, name="supprimer"),
    path("", include(router.urls)),
]
