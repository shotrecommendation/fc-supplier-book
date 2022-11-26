from django.db import models

from .abstract import RecentMixin


class Company(models.Model, RecentMixin):
    """
    Model describing and identifying suppliers.
    """

    name = models.CharField(max_length=100, help_text="Full company name.")
    short_name = models.CharField(
        max_length=10, help_text="Shortened name of the company."
    )
    year_of_foundation = models.PositiveIntegerField(
        null=True, blank=True, help_text="Year of the company's foundation."
    )
    address = models.TextField(blank=True, help_text="Full address of the company.")
    number_of_employees = models.PositiveIntegerField(
        null=True, blank=True, help_text="Approximate number of employees."
    )
    description = models.TextField(
        blank=True, help_text="Short description of the company."
    )

    def __str__(self):
        return self.name


class Story(models.Model, RecentMixin):
    """
    Model for blog-like entries for storing newses or actions taken in regards
    to a given company.
    """

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


class Employee(models.Model, RecentMixin):
    """
    Model for storing data about the employees of the companies that are followed,
    with regard to their function in the company.
    """

    FUNCTIONS = [
        ("SERV", "serviceman"),
        ("ENGI", "engineer"),
        ("SALE", "salesman"),
        ("MANA", "management"),
        ("RCPT", "reception"),
        ("SECU", "security"),
        ("UNKN", "unknown"),
    ]

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    function = models.CharField(
        max_length=4,
        choices=FUNCTIONS,
        default="UNKN",
        help_text="Function in the company.",
    )
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=64)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.company.short_name})"


class Roadmap(models.Model):
    """
    Model for storing data about the future goals of the followed companies
    together with an approximate timeline for the actions regarding these goals.
    """

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
