from django import forms

class DadosUsuarioForm(forms.Form):
    nome = forms.CharField(max_length=80)
    salario_bruto = forms.DecimalField(required=True)
    numero_deps = forms.IntegerField(required=False)