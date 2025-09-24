from django.db import models

# Create your models here.

class Product(models.Model):
    barcode = models.CharField(max_length=64, unique=True, db_index=True)
    name = models.CharField(max_length=200, blank=True)
    provider = models.CharField(max_length=200, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.barcode} - {self.name or 'sin nombre'}"
