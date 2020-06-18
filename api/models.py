from django.db import models

class ImpostoRenda(models.Model):
    nome = models.CharField(max_length=100)
    salario_bruto = models.FloatField() 
    numero_deps = models.IntegerField()
    data_consulta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome