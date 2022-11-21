import pytest
from pytest_factoryboy import register

from catalog.tests.factories import CompanyFactory, StoryFactory

register(CompanyFactory)
register(StoryFactory)
