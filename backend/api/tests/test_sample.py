import pytest

from backend.api.models from Rating, Movie, Profile


@pytest.mark.django_db
class TestBasicModels:

    def test_profiles():
        profiles = Profile.objects.all()
        assert profiles[0].id == 1

    def test_movies():
        assert movie[0].id == 1

    def test_ratings():
        assert rating[0].id == 1
