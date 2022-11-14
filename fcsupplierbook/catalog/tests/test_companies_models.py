import pytest
from catalog.models.companies import Company
from datetime import date


@pytest.mark.django_db
def test_correct_company(company_factory):
    company = company_factory.create()
    assert Company.objects.count() == 1
