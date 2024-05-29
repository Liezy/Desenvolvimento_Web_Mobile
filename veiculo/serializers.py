
from rest_framework import serializers
from veiculo.models import Veiculo

class SerializadorVeiculo(serializers.ModelSerializer):
    """
    Serializador para o model Veiculo
    """

    class Meta:
        model = Veiculo
        exclude = []