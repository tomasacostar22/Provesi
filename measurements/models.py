from django.db import models

# Create your models here.

class InventoryEntry(models.Model):
    product = models.ForeignKey("variables.Product", on_delete=models.PROTECT, related_name="entries")
    quantity = models.PositiveIntegerField(default=1)
    provider = models.CharField(max_length=200, blank=True)
    scanned_at = models.DateTimeField(auto_now_add=True)
    duration_ms = models.PositiveIntegerField(default=0)  # tiempo de registro (lado servidor)
    scenario = models.CharField(max_length=20, blank=True, default="")  # "normal" o "overloaded" para pruebas

    class Meta:
        indexes = [
            models.Index(fields=["scanned_at"]),
            models.Index(fields=["scenario"]),
        ]
