import random
import re

import factory
from faker import Faker

from catalog.models.companies import Company, Employee, Story, Roadmap

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
    Story model factory with all parameters filled in with random values.
    """

    class Meta:
        model = Story

    company = factory.SubFactory(CompanyFactory)
    title = fake.sentence(nb_words=10)
    full_description = fake.paragraphs(nb=3)


class EmployeeFactory(factory.django.DjangoModelFactory):
    """
    Employee model factory with all parameters filled in with random values.
    """

    class Meta:
        model = Employee

    company = factory.SubFactory(CompanyFactory)
    first_name = fake.first_name()
    last_name = fake.last_name()
    function = Employee.FUNCTIONS[random.randint(0, 6)][0]
    phone_number = fake.msisdn()
    email = f"{first_name}.{last_name}@example.com"


class RoadmapFactory(factory.django.DjangoModelFactory):
    """
    Roadmap model factory with all fields filled in with random values.
    """

    class Meta:
        model = Roadmap

    company = factory.SubFactory(CompanyFactory)
    goal_title = fake.sentence(nb_words=6)
    additional_info = fake.paragraph()
    start_year = fake.date_between(start_date="-5y", end_date="+5y").year
    end_year = fake.date_between(start_date="+5y", end_date="+15y").year
