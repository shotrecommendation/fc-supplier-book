from django.db import models
from .abstract import Product


class Battery(Product):
    """
    Model describing specific battery technical parameters.
    """

    total_energy = models.PositiveIntegerField("Total energy [kWh]")

    def __str__(self):
        return f"{self.company.short_name} - {self.model_name} ({self.total_energy}kWh)"


class FuelCell(Product):
    """
    Model describing specific fuel cell technical parameters.
    """

    rated_power = models.PositiveIntegerField("Rated power [kW]")

    def __str__(self):
        return f"{self.company.short_name} - {self.model_name} ({self.rated_power}kW)"
