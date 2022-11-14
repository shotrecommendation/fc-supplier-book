import re

import factory
from faker import Faker

from catalog.models.companies import Company, Story

fake = Faker()


class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company

    name = fake.company()
    short_name = name if len(name) <= 10 else name[:9]
    year_of_foundation = fake.past_date("-100y").year
    address = fake.address()
    number_of_employees = fake.random_int(min=10, max=10000)
    description = fake.paragraph()
