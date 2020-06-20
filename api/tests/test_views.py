from django.test import TestCase, Client

class IndexApiViewTest(TestCase):
    """
    Testando os calculos e retornos da API
    """
    def setUp(self):
        client = Client()
        
        # Teste da requisicao normal, via API
        self.data1 = {
            "nome": "Fulano",
            "salario_bruto": 5000.00,
            "numero_deps": 1
        }
        self._post1 = client.post('/api/v1/irrf/resultado', self.data1)
        self._return1 = "'Olá <strong>Fulano</strong>, a alíquota para o salário de <strong>R$ 5000.00</strong> " \
                        "é de <strong>27.5%</strong>.<br> A parcela a deduzir é de <strong>R$ 869.36</strong>.<br> " \
                        "O valor de desconto por dependente é de <strong>R$ 189.59</strong> (1 dependente(s) - valor total: " \
                        "<strong>R$ 189.59</strong>).<br> O valor do IR a ser descontado é de <strong>R$ 506</strong>.<br> " \
                        "Seu salário líquido será de <strong>R$ 4304.41</strong>.'"

        # Testando o retorno para a chamada via jQuery e aliquota = 7.5
        self.data2 = {
            "nome": "Fulano",
            "salario_bruto": 2000.00,
            "javascript": "true"
        }
        self._post2 = client.post('/api/v1/irrf/resultado', self.data2)

        # Testando aliquota = 0
        self.data3 = {
            "nome": "Fulano",
            "salario_bruto": 1000.00,
        }
        self._post3 = client.post('/api/v1/irrf/resultado', self.data3)

        # Testando aliquota = 22.5 e parcela a deduzir
        self.data4 = {
            "nome": "Fulano",
            "salario_bruto": 4000.00,
        }
        self._post4 = client.post('/api/v1/irrf/resultado', self.data4)

        # Testando aliquota = 15
        self.data5 = {
            "nome": "Fulano",
            "salario_bruto": 3000.00,
        }
        self._post5 = client.post('/api/v1/irrf/resultado', self.data5)

    def test_result_post_data(self):
        """
        Testando a mensagem de retorno
        """
        self.assertTrue(self._post1.data['mensagem'], self._return1)

    def test_http_return_api(self):
        """
        Testando o codigo de retorno http da API
        """
        self.assertTrue(self._post2.status_code, 200)

    def test_result_aliquota_0(self):
        """
        Testando o retorno da aliquota = 0
        """
        self.assertEqual(self._post3.data['aliquota'], 0)

    def test_result_aliquota_15(self):
        """
        Testando o retorno da aliquota = 15%
        """
        self.assertEqual(self._post5.data['aliquota'], 15)

    def test_result_parcela_deduzir(self):
        """
        Testando o valor da parcela a deduzir do IR
        """
        self.assertEqual(self._post4.data['parcela_deduzir'], 636.13)

        