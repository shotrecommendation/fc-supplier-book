from django.db import models
from .companies import Company


class Product(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.PROTECT, help_text="Company owning the product."
    )
    model_name = models.CharField(
        max_length=32, help_text="Company's name for the product."
    )

    class Meta:
        abstract = True


class Battery(Product):
    total_energy = models.PositiveIntegerField("Total energy [kWh]")

    def __str__(self):
        return f"{self.model_name} ({self.total_energy})"


class FuelCell(Product):
    rated_power = models.PositiveIntegerField("Rated power [kW]")

    def __str__(self):
        return f"{self.model_name} ({self.rated_power})"
