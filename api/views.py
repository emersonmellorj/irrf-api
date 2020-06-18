from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from decimal import Decimal

# Create your views here.
class IndexAPIView(APIView):
    """
    Class Based View que ira receber os dados, realizar os cálculos e retornar os dados
    """
    def post(self, request):
        data = request.data
        nome = data['nome']
        salario_bruto = data['salario_bruto'] 
        numero_deps = data['numero_deps']
        valor_deps = 0
        parcela_dependente = 189.59

        aliquota, parcela_deduzir = self.get_aliquota(salario_bruto)        

        if numero_deps > 0:
            valor_deps = numero_deps * parcela_dependente

        # Calculos
        calculo_irrf = round((Decimal(salario_bruto) * Decimal(aliquota) / 100 ) - Decimal(parcela_deduzir), 2)
        irrf = round(Decimal(calculo_irrf) + Decimal(valor_deps), 2)
        salario_liquido = round(Decimal(salario_bruto) - Decimal(irrf), 2)
    
        context = {
            'mensagem': f"A alíquota para o salário de R$ {salario_bruto} é de {aliquota}%, a parcela a deduzir é de "
                        f"R$ {parcela_deduzir}, o valor de desconto por dependente é de R$ {parcela_dependente} "
                        f"({numero_deps} dependente(s) - valor total: R$ {valor_deps}) e o valor do IR a "
                        f"ser descontado é de R$ {calculo_irrf}."
                        f" Seu salário líquido será de R$ {salario_liquido}."
        }

        response = Response(context, status=status.HTTP_200_OK)
        return response


    def get_aliquota(self, salario_bruto):
        """
        Função que irá retornar a alíquota e a parcela a deduzir
        """
        if salario_bruto <= '1.903,98':
            aliquota = 0
            parcela_deduzir = 0
        elif salario_bruto >= '1.903,98' and salario_bruto <= '2.826,65':
            aliquota = 7.5
            parcela_deduzir = 142.80
        elif salario_bruto >= '2.826,66' and salario_bruto <= '3.751,05':
            aliquota = 15
            parcela_deduzir = 354.80
        elif salario_bruto >= '3.751,06' and salario_bruto <= '4.664,69':
            aliquota = 22.5
            parcela_deduzir = 636.13
        else:
            aliquota = 27.5
            parcela_deduzir = 869.36

        return aliquota, parcela_deduzir



# {
#  "nome": "Emerson",
#  "salario_bruto": "1.400,00",
#  "numero_deps": 2
# }