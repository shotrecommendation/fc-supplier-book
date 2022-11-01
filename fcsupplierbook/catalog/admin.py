from django.contrib import admin
from .models import (
    Company,
    Story,
    Employee,
    Roadmap,
    Pricing,
    Battery,
    FuelCell,
)

admin.site.register(Company)
admin.site.register(Story)
admin.site.register(Employee)
admin.site.register(Roadmap)
admin.site.register(Pricing)
admin.site.register(Battery)
admin.site.register(FuelCell)
