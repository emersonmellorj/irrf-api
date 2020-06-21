from django import forms

class DadosUsuarioForm(forms.Form):
    """
    Formulário que os usuários irão preencher os dados para o cálculo
    """
    nome = forms.CharField(max_length=80)
    salario_bruto = forms.DecimalField(label="Salário Bruto", help_text="Exemplo: 1400.00", required=True)
    numero_deps = forms.IntegerField(label="Número de dependentes",required=False)