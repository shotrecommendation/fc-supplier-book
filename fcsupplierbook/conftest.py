import pytest
from pytest_factoryboy import register

from catalog.tests.factories import CompanyFactory

register(CompanyFactory)
