from rest_framework import serializers
from .models import Registro_cliente

class Registro_clienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Registro_cliente
        fields='__all__'