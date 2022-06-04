from django.db import models

# Create your models here.

class receta_1a3(models.Model):
    nombre = models.CharField(max_length = 20)
    ingrediente_1 = models.FloatField()
    ingrediente_2 = models.FloatField()
    ingrediente_3 = models.FloatField()
    descripcion = models.CharField(max_length = 100)
    
class receta_3a6(models.Model):
    nombre = models.CharField(max_length = 20)
    ingrediente_1 = models.FloatField()
    ingrediente_2 = models.FloatField()
    ingrediente_3 = models.FloatField()
    ingrediente_4 = models.FloatField()
    ingrediente_5 = models.FloatField()
    ingrediente_6 = models.FloatField()
    descripcion = models.CharField(max_length = 200)
    
class receta_6a10(models.Model):
    nombre = models.CharField(max_length = 20)
    ingrediente_1 = models.FloatField()
    ingrediente_2 = models.FloatField()
    ingrediente_3 = models.FloatField()
    ingrediente_4 = models.FloatField()
    ingrediente_5 = models.FloatField()
    ingrediente_6 = models.FloatField()
    ingrediente_7 = models.FloatField()
    ingrediente_8 = models.FloatField()
    ingrediente_9 = models.FloatField()
    ingrediente_10 = models.FloatField()
    descripcion = models.CharField(max_length = 300)