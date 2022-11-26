import pytest
from pytest_factoryboy import register

from catalog.tests.factories import (CompanyFactory, EmployeeFactory,
                                     StoryFactory, RoadmapFactory)

register(CompanyFactory)
register(StoryFactory)
register(EmployeeFactory)
register(RoadmapFactory)
