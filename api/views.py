from django.views.generic import FormView
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from decimal import Decimal
from .forms import DadosUsuarioForm

class IndexView(FormView):
    """
    View que renderiza a pagina inicial com o formulário a ser preenchido
    """
    template_name = 'index.html'
    form_class = DadosUsuarioForm


class IndexAPIView(APIView):
    """
    Class Based View que ira receber os dados, realizar os cálculos e retornar os dados
    """

    def post(self, request, format=None, **kwargs):
        data = request.data
        nome = data['nome']
        javascript = False

        if data.get("javascript"):
            javascript = data['javascript']

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

        # Calculo se existe aliquota e parcela a deduzir
        if aliquota > 0:
            calculo_irrf = round((Decimal(salario_bruto) * Decimal(aliquota) / 100 ) - Decimal(parcela_deduzir))

        # Somo o valor calculado acima com o valor a ser deduzido por número de dependentes 
        irrf = round(Decimal(calculo_irrf) + Decimal(valor_deps), 2)
        # Salario líquido total
        salario_liquido = round(Decimal(salario_bruto) - Decimal(irrf), 2)
    
        form = DadosUsuarioForm()
        
        context = {
            'mensagem': f"Olá <strong>{nome}</strong>, a alíquota para o salário de <strong>R$ {salario_bruto}</strong> "
                        f"é de <strong>{aliquota}%</strong>."
                        "<br> A parcela a deduzir é de "
                        f"<strong>R$ {parcela_deduzir}</strong>.<br> O valor de desconto por "
                        f"dependente é de <strong>R$ {parcela_dependente}</strong> "
                        f"({numero_deps} dependente(s) - valor total: <strong>R$ {valor_deps}</strong>).<br> "
                        "O valor do IR a "
                        f"ser descontado é de <strong>R$ {calculo_irrf}</strong>.<br>"
                        f" Seu salário líquido será de <strong>R$ {salario_liquido}</strong>.",
        }

        if javascript:
            return JsonResponse(context)
        else:
            return Response(context)
        
    
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