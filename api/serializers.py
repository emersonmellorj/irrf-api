from rest_framework import serializers

#from drf_braces.forms.serializer_form import SerializerForm

class ImpostoRendaSerializer(serializers.Serializer):
    class Meta:
        fields = (
            'nome',
            'salario_bruto',
            'numero_deps'
        )

#class ImpostoRendaForm(SerializerForm):
#    class Meta(object):
#        serializer = ImpostoRendaSerializer


