from django.db import models
from .products import Battery, FuelCell
from decimal import Decimal

CURRENCY = [
    ("EUR", "EUR"),
    ("USD", "USD"),
    ("PLN", "PLN"),
]


class Pricing(models.Model):
    date = models.DateField(help_text="Date that the offer was made.")
    expiration_date = models.DateField(help_text="Date that the offer will expire.")
    indicative_pricing = models.DecimalField(
        max_digits=16, decimal_places=2, help_text="indicative_pricing."
    )
    pricing_currency = models.CharField(
        max_length=3, choices=CURRENCY, help_text="Currency of the pricing."
    )

    class Meta:
        abstract = True

    def __str__(self):
        return f"Received on {self.date} | due to {self.expiration_date}"

    def get_recent_offers(self):
        return self.objects().order_by("-date")[3]


class BatteryPricing(Pricing):
    product = models.ForeignKey(Battery, on_delete=models.CASCADE)

    def get_cost_per_kWh(self):
        cost_per_kWh = self.indicative_pricing / self.product.total_energy
        return Decimal(cost_per_kWh).quantize(Decimal("0.01"))


class FuelCellPricing(Pricing):
    product = models.ForeignKey(FuelCell, on_delete=models.CASCADE)

    def get_cost_per_kW(self):
        cost_per_kW = self.indicative_pricing / self.product.rated_power
        return Decimal(cost_per_kWh).quantize(Decimal("0.01"))
