# App para cálculo de descontos referentes ao Imposto de Renda - Base 2020:

O app possui a seguinte estrutura: a API e backend foram desenvolvidaos com Django Rest Frameworks e o front end com HTML, CSS e Jquery.

Basicamente o aplicativo recebe os dados de nome, salário bruto e quantidade de dependentes e, quando o botão de calcular é clicado, os cálculos de deduções de imposto de renda são feitos com base na alíquota da faixa salarial e os valor de desconto por dependentes. Os valores são retornados para o usuário.

A validação dos dados do formulário é feita através de jQuery. O APP não aceita valor negativo para o campo salário bruto e o campo número de dependentes não é obrigatório.

## Links de acesso ao projeto publicado no Heroku:

Abaixo os links aonde a API e o APP estão publicados:

* Link: https://irrf-esm.herokuapp.com/  
* API: https://irrf-esm.herokuapp.com/api/v1/irrf/resultado

## Consumo da API:

Basta enviar uma requisição POST com o body em formato JSON.
Exemplo:

{
    "nome": "José da Silva",
    "salario_bruto": 4987.98,
    "numero_deps": 2 # Opcional. Caso não possua dependentes, não precisa enviar este campo 
}

O retorno será uma mensagem com os valores calculados.

## Testes automatizados:

De acordo com o coverage, o projeto esta coberto 100% pelos testes automatizados.

![Coverage Report 100%](/api/static/img/coverage_report.png "Coverage Report")

Para a execução dos testes, basta rodar localmente o comando: coverage run manage.py test

## Módulos utilizados:

1. Django Bootstrap4 para estilização do front end;
2. Django Fontawesome5, para utilização de ícones no projeto;
3. Coverage, para validação da cobertura dos testes automatizados;
4. TestCase, para criação dos testes automatizados;
5. Django Rest Framework, para o desenvolvimento da API.

## Testes de validação dos campos do Form e consumo da API:

Foi utilizado Jquery para a realização dos testes. Utilizado Ajax para realizar o consumo de API e o envio dos dados do formulário, preenchidos pelo usuário.

## Armazenamento dos dados:

Não foi necessária a utilização de banco de dados nesta solução, visto que os dados não são armazenados.