from django.contrib import admin
from api.models import Profile
from api.models import Movie
from api.models import Rating
from api.models import Like_movie
from api.models import user_based_movie
from api.models import item_based_movie
from api.models import matrix_factorization_movie
from api.models import movie_url

admin.site.register(Profile)
admin.site.register(Movie)
admin.site.register(Rating)
admin.site.register(Like_movie)
admin.site.register(user_based_movie)
admin.site.register(item_based_movie)
admin.site.register(matrix_factorization_movie)