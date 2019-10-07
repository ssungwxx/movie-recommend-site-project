from django.conf.urls import url
from api.views import movie_views
from api.views import auth_views
from api.views import rating_views
from api.views import profile_views
from api.views import like_movie_views
from api.views import classify_movies_views
from api.views import item_based_views
from api.views import user_based_views
from api.views import matrix_factorization_views

urlpatterns = [
    url('auth/signup-many/$', auth_views.signup_many, name='sign_up_many'),
    url('movies/$', movie_views.movies, name='movie_list'),
    url('ratings/$', rating_views.ratings, name='rating_list'),
    url('profiles/$', profile_views.profiles, name='profile_list'),
    url('likemovie/$', like_movie_views.like_movies, name='like_movie_list'),
    url('itembased/$', item_based_views.item_based_movies, name='item_based_list'),
    url('userbased/$', user_based_views.user_based_movies, name='user_based_list'),
    url('matrixfactorization/$', matrix_factorization_views.matrix_factorization_movies, name='matrix_factorization_list'),
    url('classify/$', classify_movies_views.classify_movies,
        name='classify_movies'),
]
