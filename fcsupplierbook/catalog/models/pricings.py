from decimal import Decimal

from django.db import models

from .abstract import Pricing
from .products import Battery, FuelCell


class BatteryPricing(Pricing):
    product = models.ForeignKey(Battery, on_delete=models.CASCADE)

    def get_cost_per_kWh(self):
        """
        Get the cost of 1kWh of battery's energy capacity based on the offer.
        """
        cost_per_kWh = self.indicative_pricing / self.product.total_energy
        return Decimal(cost_per_kWh).quantize(Decimal("0.01"))


class FuelCellPricing(Pricing):
    """
    Get the cost of 1kW of fuel cell's power based on the offer.
    """

    product = models.ForeignKey(FuelCell, on_delete=models.CASCADE)

    def get_cost_per_kW(self):
        cost_per_kW = self.indicative_pricing / self.product.rated_power
        return Decimal(cost_per_kWh).quantize(Decimal("0.01"))
