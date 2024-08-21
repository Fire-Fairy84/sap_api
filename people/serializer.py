from rest_framework import serializers
from people.models import Person


# Serializamos la data que trae ese objeto, en este caso el objeto Person
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        # Le decimos cuáles son los cmpos de mi modelo que quiero que me estructure. Serialización de la data. Aquí le decimos que queremos que serialice todos los campos
        fields = '__all__'
