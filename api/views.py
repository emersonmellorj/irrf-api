from django.shortcuts import render, redirect, reverse
from django.views.generic import FormView, TemplateView
from django.views import View
from django.http import (HttpResponse, HttpResponseRedirect, JsonResponse)
from rest_framework.views import APIView
from rest_framework.response import Response
from django.urls import reverse_lazy
from decimal import Decimal
from .forms import DadosUsuarioForm
from .serializers import ImpostoRendaSerializer

class IndexView(FormView, TemplateView):
        template_name = 'index.html'
        form_class = DadosUsuarioForm
        success_url = '/'


class IndexAPIView(APIView):
    """
    Class Based View que ira receber os dados, realizar os cálculos e retornar os dados
    """

    def post(self, request, format=None, **kwargs):
        data = request.data
        nome = data['nome']
        salario_bruto = round(Decimal(data['salario_bruto']), 2)
        
        # Se numero de dependentes nao for enviado seto para 0
        if not data.get('numero_deps'):
            numero_deps = 0
        else:
            numero_deps = int(data['numero_deps'])

        valor_deps = 0
        parcela_dependente = 189.59
        calculo_irrf = 0

        aliquota, parcela_deduzir = self.get_aliquota(salario_bruto)        

        if numero_deps > 0:
            valor_deps = numero_deps * parcela_dependente

        # Calculos se existe aliquota e parcela a deduzir
        if aliquota > 0:
            calculo_irrf = round((Decimal(salario_bruto) * Decimal(aliquota) / 100 ) - Decimal(parcela_deduzir))

        # Somo o valor calculado acima com o valor a ser deduzido por número de dependentes 
        irrf = round(Decimal(calculo_irrf) + Decimal(valor_deps), 2)
        # Salario líquido total
        salario_liquido = round(Decimal(salario_bruto) - Decimal(irrf), 2)
    
        form = DadosUsuarioForm()
        
        context = {
            'mensagem': f"A alíquota para o salário de **R$ {salario_bruto}** é de **{aliquota}%**."
                        "<br> A parcela a deduzir é de "
                        f"**R$ {parcela_deduzir}**.<br> O valor de desconto por "
                        f"dependente é de **R$ {parcela_dependente}** "
                        f"({numero_deps} dependente(s) - valor total: **R$ {valor_deps}**).<br> O valor do IR a "
                        f"ser descontado é de **R$ {calculo_irrf}**.<br>"
                        f" Seu salário líquido será de **R$ {salario_liquido}**.",
            'form': form
        }

        template_name = 'index.html'
        #content = loader.render_to_string(template_name, context)
        content = render(request, template_name, context)
        return HttpResponse(content)
        
    
    @classmethod
    def get_aliquota(self, salario_bruto):
        """
        Função que irá retornar a alíquota e a parcela a deduzir
        """
        if salario_bruto <= 1903.98:
            aliquota = 0
            parcela_deduzir = 0
        elif salario_bruto >= 1903.98 and salario_bruto <= 2826.65:
            aliquota = 7.5
            parcela_deduzir = 142.80
        elif salario_bruto >= 2826.66 and salario_bruto <= 3751.05:
            aliquota = 15
            parcela_deduzir = 354.80
        elif salario_bruto >= 3751.06 and salario_bruto <= 4664.69:
            aliquota = 22.5
            parcela_deduzir = 636.13
        else:
            aliquota = 27.5
            parcela_deduzir = 869.36

        return aliquota, parcela_deduzir



# {
#  "nome": "Emerson",
#  "salario_bruto": "1400.00",
#  "numero_deps": 2
# }