from rest_framework import serializers
from .models import ImpostoRenda

class ImpostoRendaSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'data_consulta': {'write_only': True}
        }
        model = ImpostoRenda
        fields = (
            'name',
            'salario_bruto',
            'numero_deps',
            'data_consulta'
        )

