import pytest
from django.db.utils import DataError, IntegrityError

from catalog.models.companies import Employee


@pytest.mark.django_db
def test_correct_employee(employee_factory):
    """
    Test if employees with parameters compying to initial
    model design are being added to the database.
    """
    # TEST 1: All fields provided
    employee = employee_factory.create()
    assert Employee.objects.last() == employee

    # TEST 2: No phone number provided
    employee = employee_factory.create(phone_number=None)
    assert Employee.objects.last() == employee


@pytest.mark.django_db
def test_employee_without_first_name(employee_factory):
    """
    Check, that trying to add an Employee instance without first_name given
    will result in an IntegrityError.
    """

    with pytest.raises(IntegrityError):
        employee_factory.create(first_name=None)


@pytest.mark.django_db
def test_employee_with_first_name_longer_than_20(employee_factory):
    """
    Check, that trying to add an Employee instance with first_name being longer
    than 20 signs will raise a DataError.
    """
    name_too_long = "AnUnnaturallyLongName"
    with pytest.raises(DataError):
        employee_factory.create(first_name=name_too_long)


@pytest.mark.django_db
def test_employee_without_last_name(employee_factory):
    """
    Check, that trying to add an Employee instance without last_name given
    will result in an IntegrityError.
    """

    with pytest.raises(IntegrityError):
        employee_factory.create(last_name=None)


@pytest.mark.django_db
def test_employee_with_last_name_longer_than_20(employee_factory):
    """
    Check, that trying to add an Employee instance with last_name being longer
    than 20 signs will raise a DataError.
    """
    name_too_long = "AnUnnaturallyLongName"
    with pytest.raises(DataError):
        employee_factory.create(last_name=name_too_long)


@pytest.mark.django_db
def test_employee_with_phone_number_longer_than_15(employee_factory):
    """
    Check, that trying to add an Employee instance with phone_number being longer
    than 15 signs will raise a DataError.
    """
    phone_number_too_long = "+48 123 456 7891"
    with pytest.raises(DataError):
        employee_factory.create(phone_number=phone_number_too_long)


@pytest.mark.django_db
def test_employee_with_email_longer_than_64(employee_factory):
    """
    Check, that trying to add an Employee instance with email being longer
    than 64 signs will raise a DataError.
    """
    email_too_long = (
        "anunnaturallylongname.anUnnaturallylongsurname@anunnaturallylong.domain"
    )
    with pytest.raises(DataError):
        employee_factory.create(email=email_too_long)
