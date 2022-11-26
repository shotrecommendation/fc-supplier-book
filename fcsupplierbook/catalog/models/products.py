from django.db import models

from .abstract import GenericProduct


class ProductType(models.Model):
    """
    Model allowing to define a general type/category of product that will allow
    to distinguish between different technologies, eg. Fuel Cell or Battery,
    but not being too specific, like PEM Fuel Cell, where PEM in this case would be
    a category of Fuel Cells in general.
    """

    full_name = models.CharField(
        max_length=20,
        unique=True,
        help_text="Full name of a gneral category of products, eg. Battery or Engine, but not LTO Battery or Diesel Engine.",
    )
    short_name = models.CharField(
        max_length=3,
        unique=True,
        help_text="A short name or abbreviation of the full name.",
    )

    def __str__(self):
        return self.full_name


class Product(GenericProduct):
    """
    Model describing a specific product distinguished by the product type.
    """

    product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT)

    def __str__(self):
        return (
            f"{self.company.short_name} - {self.model_name} - {product_type.full_name}"
        )


class ParameterCategory(models.Model):
    """
    A category of parameter that will enable to group newly created parameters thematically.
    For example, a parameter named Peak Power and parameter named Idle Power, could both be grouped
    under Electrical Specifications category.
    """

    name = models.CharField(max_length=32, help_text="Category of parameters.")

    def __str__(self):
        return self.name


class ProductParameter(models.Model):
    """
    A product parameter linked to a product type.
    """

    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    category = models.ForeignKey(ParameterCategory, on_delete=models.PROTECT)
    name = models.CharField(
        max_length=32,
        unique=True,
        help_text="Name of the parameter, e.g. Length or Peak Power",
    )
    unit = models.CharField(
        max_length=10, default="-", help_text="Unit of measurment if applies."
    )
    is_key_parameter = models.BooleanField(
        default=False,
        help_text="Decides if the parameter is important enough to include it in every summary view by default. If not, it will still be available in detailed views.",
    )

    def __str__(self):
        return f"{self.name} [{self.unit}]" if self.unit != "-" else self.name


class ParameterValue(models.Model):
    """
    A value of a parameter assigned to a very specific product in a database.
    """

    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    parameter_type = models.ForeignKey(ProductParameter, on_delete=models.CASCADE)
    value = models.CharField(max_length=128)

    def __str__(self):
        return self.value
