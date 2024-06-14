from django.db import models

class Product(models.Model):
    description = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    
    def __str__(self):
        return f'es un/a {self.description} y vale ${self.price}' 