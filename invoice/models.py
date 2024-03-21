from django.db import models

# Create your models here.

class Product(models.Model):
    prod_name = models.CharField('Product', max_length=255)
    unit = models.CharField('Unit', default='ea', max_length=255)
    vendor = models.CharField('Vendor', max_length=255, blank=True)
    product_is_delete = models.BooleanField(default=False)

    class Material(models.TextChoices):
        NATURAL_QUARTZITE = 'NATURAL QUARTZITE', 'Natural Quartzite'
        ENGINEERED_QUARTZ = 'ENGINEERED QUARTZ', 'Engineered Quartz'
        GRANITE = 'GRANITE', 'Granite'
        MARBLE = 'MARBLE', 'Marble'
        DOLOMITE = 'DOLOMITE', 'Dolomite'
        SOAPSTONE = 'SOAPSTONE', 'Soapstone'
        OTHER = 'OTHER', 'Other'

    material = models.CharField('Material', max_length=255, choices=Material.choices, blank=True)

    def __str__(self):
        return str(self.prod_name)
