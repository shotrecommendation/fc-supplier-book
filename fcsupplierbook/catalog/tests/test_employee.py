import pytest
from django.db.utils import IntegrityError

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
