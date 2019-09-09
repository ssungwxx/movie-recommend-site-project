from django.conf.urls import url
from api.views import movie_views
from api.views import auth_views
from api.views import rating_views
from api.views import profile_views
from api.views import classify_movies_views

urlpatterns = [
    url('auth/signup-many/$', auth_views.signup_many, name='sign_up_many'),
    url('movies/$', movie_views.movies, name='movie_list'),
    url('ratings/$', rating_views.ratings, name='rating_list'),
    url('profiles/$', profile_views.profiles, name='profile_list'),
    url('classify/$', classify_movies_views.classify_movies,
        name='classify_movies'),
]
