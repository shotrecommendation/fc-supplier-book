import pytest
from django.db.utils import IntegrityError

from catalog.models.companies import Story


@pytest.mark.django_db
def test_correct_story(story_factory):
    """
    Test if Story instance with correct parameters are saved to the database.
    """
    story_factory.create()
    assert Story.objects.count() == 1


@pytest.mark.django_db
def test_story_with_no_company_assigned(story_factory):
    """
    Test that story with no company assigned (equal to None/null) will not
    get saved to the database
    """
    with pytest.raises(IntegrityError):
        story_factory.create(company=None)


@pytest.mark.django_db
def test_story_with_no_title(story_factory):
    """
    Test that story with no title provided (equal to None/null) will not
    get saved to the database
    """
    with pytest.raises(IntegrityError):
        story_factory.create(title=None)


@pytest.mark.django_db
def test_story_with_no_full_description(story_factory):
    """
    Test that story with no full_description (equal to None/null) will not
    get saved to the database
    """
    with pytest.raises(IntegrityError):
        story_factory.create(full_description=None)
