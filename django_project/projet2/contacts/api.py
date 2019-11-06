from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Contact
from .serializers import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        auteur = self.request.user
        queryset = Contact.objects.filter(auteur=auteur)

        if queryset:
            pass
        else:
            queryset = []
        return queryset
