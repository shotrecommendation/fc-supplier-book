from django.contrib import admin

from .models.companies import Company, Employee, Roadmap, Story
from .models.products import (
    ProductType,
    Product,
    ParameterCategory,
    ProductParameter,
    ParameterValue,
)

admin.site.register(Company)
admin.site.register(Story)
admin.site.register(Employee)
admin.site.register(Roadmap)
admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(ParameterCategory)
admin.site.register(ProductParameter)
admin.site.register(ParameterValue)
