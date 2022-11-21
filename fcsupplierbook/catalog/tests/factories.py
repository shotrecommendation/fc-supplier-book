import re

import factory
from faker import Faker

from catalog.models.companies import Company, Story

fake = Faker()


class CompanyFactory(factory.django.DjangoModelFactory):
    """
    Company model factory with all parameters filled in with random values.
    """

    class Meta:
        model = Company

    name = fake.company()
    short_name = name if len(name) <= 10 else name[:9]
    year_of_foundation = fake.past_date("-100y").year
    address = fake.address()
    number_of_employees = fake.random_int(min=10, max=10000)
    description = fake.paragraph()


class StoryFactory(factory.django.DjangoModelFactory):
    """
    Story model factory with all parameters filled in with random values
    except for the company ForeignKey, which has to be assigned during
    build or creation.
    """

    class Meta:
        model = Story

    company = factory.SubFactory(CompanyFactory)
    title = fake.sentence(nb_words=10)
    full_description = fake.paragraphs(nb=3)
