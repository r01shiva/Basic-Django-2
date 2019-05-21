from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=250)
    image = models.FileField()
    form = models.CharField(max_length=20,default='Liquid')
    quantity = models.CharField(max_length=20,default='')
    pack = models.CharField(max_length=20,default='')
    usage = models.CharField(max_length=30,default='')
    description = models.CharField(max_length=500,default='')
    price = models.DecimalField(max_digits=5, decimal_places=2)


    def __str__(self):
        return self.name + '-' + str(self.id)

