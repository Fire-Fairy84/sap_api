from rest_framework import viewsets
from .serializer import PersonSerializer
from .models import Person


class PersonView(viewsets.ModelViewSet):
    serializer_class = PersonSerializer

    # Usar modelo a través del ORM
    queryset = Person.objects.all()
