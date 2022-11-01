from django.contrib import admin
from .models.companies import Company, Employee, Story, Roadmap
from .models.products import Battery, FuelCell
from .models.pricings import BatteryPricing, FuelCellPricing

admin.site.register(Company)
admin.site.register(Story)
admin.site.register(Employee)
admin.site.register(Roadmap)
admin.site.register(Battery)
admin.site.register(FuelCell)
admin.site.register(BatteryPricing)
admin.site.register(FuelCellPricing)
