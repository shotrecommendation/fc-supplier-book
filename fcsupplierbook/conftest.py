import pytest
from pytest_factoryboy import register

from catalog.tests.factories import (CompanyFactory, EmployeeFactory,
                                     StoryFactory)

register(CompanyFactory)
register(StoryFactory)
register(EmployeeFactory)
