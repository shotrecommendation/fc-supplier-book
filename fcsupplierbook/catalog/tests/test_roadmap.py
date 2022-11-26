import pytest

from django.db.utils import DataError, IntegrityError
from catalog.models.companies import Roadmap

@pytest.mark.django_db
def test_correct_roadmap_entry(roadmap_factory):
    """
    Check if Roadmap instance with all fields filled in correctly is
    being added to the database.
    """
    # TEST 1: all fields filled in
    roadmap = roadmap_factory.create()
    assert Roadmap.objects.last() == roadmap

    # TEST 2: start_year field empty
    roadmap = roadmap_factory.create(start_year=None)
    assert Roadmap.objects.last() == roadmap

    # TEST 3: end_year field empty
    roadmap = roadmap_factory.create(end_year=None)
    assert Roadmap.objects.last() == roadmap


@pytest.mark.django_db
def test_goal_title_empty(roadmap_factory):
    """
    Check that Roadmap instance with goal_title field empty will
    raise an IntegrityError.
    """
    with pytest.raises(IntegrityError):
        roadmap_factory.create(goal_title=None)


@pytest.mark.django_db
def test_additional_info_empty(roadmap_factory):
    """
    Check that Roadmap instance with additional_info field empty will
    raise an IntegrityError.
    """
    with pytest.raises(IntegrityError):
        roadmap_factory.create(additional_info=None)


@pytest.mark.django_db
def test_goal_title_longer_than_64(roadmap_factory):
    """
    Check that Roadmap instance with goal_title field longer than 64 signs
    will raise an DataError.
    """
    goal_title_too_long = "This goal title is over 64 long - the roadmap should not be added"
    with pytest.raises(DataError):
        roadmap_factory.create(goal_title=goal_title_too_long)