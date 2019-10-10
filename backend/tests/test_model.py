import pytest

from api.models import Movie, Profile, Rating


@pytest.mark.django_db
class MovieModel:
    def test_new_movie(self, movies):
        assert movies.movie_id == 1
        assert movies.movie_id == 2
        assert Movie.objects.count() > 0
