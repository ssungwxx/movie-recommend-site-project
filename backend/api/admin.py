from django.contrib import admin
from api.models import Profile
from api.models import Movie
from api.models import Rating

admin.site.register(Profile)
admin.site.register(Movie)
admin.site.register(Rating)