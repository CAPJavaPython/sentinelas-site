from django.db import models

# Create your models here.
class Integrante(models.Model):
    nome = models.CharField(max_length=100)
    birth_date = models.DateField()
    telefone = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name