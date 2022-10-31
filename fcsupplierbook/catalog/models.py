from django.db import models


PRODUCT_TYPE = [
    ("FCM", "fuel cell module"),
    ("BAT", "battery pack"),
]

CURRENCY = [
    ("EUR", "EUR"),
    ("USD", "USD"),
    ("PLN", "PLN"),
]


class Company(models.Model):
    name = models.CharField(max_length=100, help_text="Full company name.")
    short_name = models.CharField(
        max_length=10, help_text="Shortened name of the company."
    )
    date_of_foundation = models.DateField(help_text="Date of the company's foundation.")
    address = models.CharField(max_length=256, help_text="Full address of the company.")
    number_of_employees = models.PositiveIntegerField(
        null=True, blank=True, help_text="Approximate number of employees."
    )
    description = models.TextField(help_text="Short description of the company.")
    last_modified = models.DateField(auto_now=True)

    def get_recently_modified(self):
        return self.objects().order_by("-last_modified")[0]


class Story(models.Model):
    title = models.CharField(max_length=128, help_text="Short summary of the entry.")
    full_description = models.TextField(help_text="Full description of the event.")
    date = models.DateField(auto_now_add=True, help_text="Date of the entry.")
    company = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
        help_text="Choose a company that the entry is connected to.",
    )

    def get_recent_stories(self):
        return self.objects().order_by("-date")[3]


class Product(models.Model):
    product_type = models.CharField(max_length=3, choices=PRODUCT_TYPE)
    model_name = models.CharField(
        max_length=32, help_text="Company's name for the product."
    )
    company = models.ForeignKey(
        Company, on_delete=models.PROTECT, help_text="Company owning the product."
    )


class Pricing(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField(help_text="Date that the offer was made.")
    expiration_date = models.DateField(help_text="Date that the offer will expire.")
    indicative_pricing = models.DecimalField(
        max_digits=16, decimal_places=2, help_text="indicative_pricing."
    )
    pricing_currency = models.CharField(
        max_length=3, choices=CURRENCY, help_text="Currency of the pricing."
    )

    def __str__(self):
        return f"Received on {self.date} | due to {self.expiration_date}"

    def get_recent_offers(self):
        return self.objects().order_by("-date")[3]


class Battery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total_energy = models.PositiveIntegerField("Total energy [kWh]")

    def __str__(self):
        return f"{self.product.model_name} ({self.total_energy})"


class FuelCell(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rated_power = models.PositiveIntegerField("Rated power [kW]")

    def __str__(self):
        return f"{self.product.model_name} ({self.rated_power})"


class Employee(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=32, help_text="Function in the company.")
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=64)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.company.short_name})"
