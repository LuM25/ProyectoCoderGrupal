from django.db import models

# Create your models here.

class receta_1a3(models.Model):
    nombre = models.CharField(max_length = 20)
    ingrediente_1 = models.CharField(max_length = 30, default = '')
    cantidad_1 = models.FloatField(null=True , blank = True)
    ingrediente_2 = models.CharField(max_length = 30)
    cantidad_2 = models.FloatField(null=True , blank = True)
    ingrediente_3 = models.CharField(max_length = 30)
    cantidad_3 = models.FloatField(null=True , blank = True)
    procedimiento = models.CharField(max_length = 500,null=True , blank = True)
    
class receta_4a6(models.Model):
    nombre = models.CharField(max_length = 20)
    ingrediente_1 = models.CharField(max_length = 30)
    cantidad_1 = models.FloatField(null=True , blank = True)
    ingrediente_2 = models.CharField(max_length = 30)
    cantidad_2 = models.FloatField(null=True , blank = True)
    ingrediente_3 = models.CharField(max_length = 30)
    cantidad_3 = models.FloatField(null=True , blank = True)
    ingrediente_4 = models.CharField(max_length = 30)
    cantidad_4 = models.FloatField(null=True , blank = True)
    ingrediente_5 = models.CharField(max_length = 30)
    cantidad_5 = models.FloatField(null=True , blank = True)
    ingrediente_6 = models.CharField(max_length = 30)
    cantidad_6 = models.FloatField(null=True , blank = True)
    procedimiento = models.CharField(max_length = 500,null=True , blank = True)

    
class receta_7a10(models.Model):
    nombre = models.CharField(max_length = 20)
    ingrediente_1 = models.CharField(max_length = 30)
    cantidad_1 = models.FloatField(null=True , blank = True)
    ingrediente_2 = models.CharField(max_length = 30)
    cantidad_2 = models.FloatField(null=True , blank = True)
    ingrediente_3 = models.CharField(max_length = 30)
    cantidad_3 = models.FloatField(null=True , blank = True)
    ingrediente_4 = models.CharField(max_length = 30)
    cantidad_4 = models.FloatField(null=True , blank = True)
    ingrediente_5 = models.CharField(max_length = 30)
    cantidad_5 = models.FloatField(null=True , blank = True)
    ingrediente_6 = models.CharField(max_length = 30)
    cantidad_6 = models.FloatField(null=True , blank = True)
    ingrediente_7 = models.CharField(max_length = 30)
    cantidad_7 = models.FloatField(null=True , blank = True)
    ingrediente_8 = models.CharField(max_length = 30)
    cantidad_8 = models.FloatField(null=True , blank = True)
    ingrediente_9 = models.CharField(max_length = 30)
    cantidad_9 = models.FloatField(null=True , blank = True)
    ingrediente_10 = models.CharField(max_length = 30)
    cantidad_10 = models.FloatField(null=True , blank = True)
    procedimiento = models.CharField(max_length = 500,null=True , blank = True)
