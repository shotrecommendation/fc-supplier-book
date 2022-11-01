from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

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
    year_of_foundation = models.PositiveIntegerField(
        help_text="Year of the company's foundation."
    )
    address = models.TextField(help_text="Full address of the company.")
    number_of_employees = models.PositiveIntegerField(
        null=True, blank=True, help_text="Approximate number of employees."
    )
    description = models.TextField(help_text="Short description of the company.")
    last_modified = models.DateField(auto_now=True)

    def get_recently_modified(self):
        return self.objects().order_by("-last_modified")[0]

    def __str__(self):
        return self.name


class Story(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
    )
    title = models.CharField(max_length=128, help_text="Short summary of the entry.")
    full_description = models.TextField(help_text="Full description of the event.")
    date = models.DateField(auto_now_add=True, help_text="Date of the entry.")

    def get_recent_stories(self):
        return self.objects().order_by("-date")[3]

    def __str__(self):
        return self.title


class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    job_title = models.CharField(max_length=32, help_text="Function in the company.")
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=64)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.company.short_name})"


class Roadmap(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    goal_title = models.CharField(
        max_length=64,
        blank=False,
        help_text="Short summary of a general goal of a company.",
    )
    additional_info = models.TextField()
    start_year = models.PositiveIntegerField(
        help_text="The year, that the work on this goal is planned to start."
    )
    end_year = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text="The year, that the work on this goal is planned to end.",
    )

    def __str__(self):
        time_period = (
            f"[{self.start_year} - {self.end_year}]"
            if self.end_year
            else f"[{self.start_year}]"
        )
        return f"{time_period} {self.goal_title}"


class Product(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.PROTECT, help_text="Company owning the product."
    )
    model_name = models.CharField(
        max_length=32, help_text="Company's name for the product."
    )

    class Meta:
        abstract = True


class Pricing(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    product = GenericForeignKey()
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


class Battery(Product):
    total_energy = models.PositiveIntegerField("Total energy [kWh]")

    def __str__(self):
        return f"{self.model_name} ({self.total_energy})"


class FuelCell(Product):
    rated_power = models.PositiveIntegerField("Rated power [kW]")

    def __str__(self):
        return f"{self.model_name} ({self.rated_power})"
