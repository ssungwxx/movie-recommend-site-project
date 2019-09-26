from django.contrib import admin
from api.models import Profile
from api.models import Movie
from api.models import Rating
from api.models import Like_movie

admin.site.register(Profile)
admin.site.register(Movie)
admin.site.register(Rating)
admin.site.register(Like_movie)