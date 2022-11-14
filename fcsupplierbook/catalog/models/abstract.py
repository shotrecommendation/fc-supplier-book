from django.db import models
from django.utils import timezone


class RecentMixin:
    """
    Abstract class mixin allowing models to store info about the
    date of the last modification and to retreive a specified
    number of recently added/modified instances of the given model.
    """

    last_modified = models.DateField(auto_now=True)

    def get_recently_modified(self, requested_number: int = 3):
        """
        Get the X recently added/modified instances of a model,
        where X is defined by the requested_number parameter.
        """
        return self.objects().order_by("-last_modified")[requested_number]


class Product(models.Model, RecentMixin):
    """
    Abstract class defining the base for the product models of various suppliers.
    """

    company = models.ForeignKey(
        "Company", on_delete=models.PROTECT, help_text="Company owning the product."
    )
    model_name = models.CharField(
        max_length=32, help_text="Company's name for the product."
    )
    last_modified = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Pricing(models.Model, RecentMixin):
    """
    Abstract class defining the base for the pricing models of various products.
    """

    CURRENCY = [
        ("EUR", "EUR"),
        ("USD", "USD"),
        ("PLN", "PLN"),
    ]

    received_date = models.DateField(help_text="Date that the offer was made.")
    expiration_date = models.DateField(help_text="Date that the offer will expire.")
    volume = models.PositiveIntegerField(
        help_text="Volume on which the offer is based."
    )
    indicative_pricing = models.DecimalField(max_digits=16, decimal_places=2)
    pricing_currency = models.CharField(
        max_length=3, choices=CURRENCY, help_text="Currency of the pricing."
    )

    class Meta:
        abstract = True

    def __str__(self):
        return f"Received on {self.received_date} | due to {self.expiration_date}"

    def is_valid(self):
        """
        Return True if the offer is still valid (if the expiration date is in the
        future compared to the current date. Return False otherwise.)
        """
        time = timezone.now().date()
        return True if self.expiration_date - time >= 0 else False
