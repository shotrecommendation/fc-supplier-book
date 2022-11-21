from datetime import date

import pytest
from django.db.utils import DataError, IntegrityError

from catalog.models.companies import Company


@pytest.mark.django_db
def test_correct_company(company_factory):
    """
    Test if companies with parameters compying to initial
    model design are being added to the database.
    """
    # TEST 1: All parameters filled in
    company = company_factory.create()
    assert Company.objects.last() == company

    # TEST 2: Blank value in address field
    company = company_factory.create(address="")
    assert Company.objects.last() == company

    # TEST 3: Null value for the year_of_foundation
    company = company_factory.create(year_of_foundation=None)
    assert Company.objects.last() == company

    # TEST 4: Null value for the number_of_employees
    company = company_factory.create(number_of_employees=None)
    assert Company.objects.last() == company

    # TEST 5: Blank value in description field
    company = company_factory.create(description="")
    assert Company.objects.last() == company


@pytest.mark.django_db
def test_short_name_length_over_10(company_factory):
    """
    Test if companies with short_name being longer than
    10 characters are NOT being added to the database.
    """
    with pytest.raises(
        DataError, match="value too long for type character varying\\(10\\)"
    ):
        company_factory.create(short_name="Short name too long")


@pytest.mark.django_db
def test_short_name_null(company_factory):
    """
    Test if companies with short_name == null are NOT being added to the database.
    """
    with pytest.raises(IntegrityError):
        company_factory.create(short_name=None)


@pytest.mark.django_db
def test_address_null(company_factory):
    """
    Test if companies with address == null are NOT being added to the database.
    """
    with pytest.raises(IntegrityError):
        company_factory.create(address=None)


@pytest.mark.django_db
def test_negative_number_of_employees(company_factory):
    """
    Test if companies with number_of_employees lower than 0
    are NOT being added to the database.
    """
    with pytest.raises(IntegrityError):
        company_factory.create(number_of_employees=-1)


@pytest.mark.django_db
def test_negative_year_of_foundation(company_factory):
    """
    Test if companies with year_of_foundation lower than 0
    are NOT being added to the database.
    """
    with pytest.raises(IntegrityError):
        company_factory.create(year_of_foundation=-1)


@pytest.mark.django_db
def test_description_null(company_factory):
    """
    Test if companies with description == null are NOT being added to the database.
    """
    with pytest.raises(IntegrityError):
        company_factory.create(description=None)
