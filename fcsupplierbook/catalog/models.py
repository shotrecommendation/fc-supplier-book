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
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=10)
    date_of_foundation = models.DateField()
    address = models.CharField(max_length=256)
    number_of_employees = models.PositiveIntegerField()


class Story(models.Model):
    title = models.CharField(max_length=128)
    full_description = models.TextField()
    date = models.DateField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)


class Product(models.Model):
    product_type = models.CharField(max_length=3, choices=PRODUCT_TYPE)
    model_name = models.CharField(max_length=32)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    indicative_pricing = models.DecimalField(max_digits=16, decimal_places=2)
    pricing_currency = models.CharField(max_length=3, choices=CURRENCY)


class Employee(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=64)
