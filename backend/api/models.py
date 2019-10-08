from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, default='M')
    age = models.IntegerField(default=25)
    occupation = models.CharField(max_length=200)


#  wrapper for create user Profile
def create_profile(**kwargs):
    user = User.objects.create_user(
        username=kwargs['username'],
        password=kwargs['password'],
        is_active=True,
    )

    profile = Profile.objects.create(user=user,
                                     gender=kwargs['gender'],
                                     age=kwargs['age'],
                                     occupation=kwargs['occupation'])

    return profile


class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    genres = models.CharField(max_length=500)

    @property
    def genres_array(self):
        return self.genres.strip().split('|')


class Rating(models.Model):
    userid = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='rating_user')
    movieid = models.ForeignKey(Movie,
                                on_delete=models.CASCADE,
                                related_name='ratings')
    rating = models.IntegerField(default=0)
    timestamp = models.DateTimeField(blank=True)

    def __str__(self):
        return '%s :%d' % ('rating', self.rating)

class Like_movie(models.Model):
    movieid = models.IntegerField(primary_key=True)
    rank1 = models.IntegerField(default = 0)
    rank2 = models.IntegerField(default = 0)
    rank3 = models.IntegerField(default = 0)
    rank4 = models.IntegerField(default = 0)
    rank5 = models.IntegerField(default = 0)
    rank6 = models.IntegerField(default = 0)
    rank7 = models.IntegerField(default = 0)
    rank8 = models.IntegerField(default = 0)
    rank9 = models.IntegerField(default = 0)
    rank10 = models.IntegerField(default = 0)


class item_based_movie(models.Model):
    movieid = models.IntegerField(primary_key=True)
    rank1 = models.IntegerField(default = 0)
    rank2 = models.IntegerField(default = 0)
    rank3 = models.IntegerField(default = 0)
    rank4 = models.IntegerField(default = 0)
    rank5 = models.IntegerField(default = 0)

class user_based_movie(models.Model):
    movieid = models.IntegerField(primary_key=True)
    rank1 = models.IntegerField(default = 0)
    rank2 = models.IntegerField(default = 0)
    rank3 = models.IntegerField(default = 0)
    rank4 = models.IntegerField(default = 0)
    rank5 = models.IntegerField(default = 0)

class matrix_factorization_movie(models.Model):
    movieid = models.IntegerField(primary_key=True)
    rank1 = models.IntegerField(default = 0)
    rank2 = models.IntegerField(default = 0)
    rank3 = models.IntegerField(default = 0)
    rank4 = models.IntegerField(default = 0)
    rank5 = models.IntegerField(default = 0)

    
class movie_url(models.Model):
    movieid = models.IntegerField(primary_key=True)
    url = models.CharField(max_length=300)

class Item(models.Model):
    name = models.CharField(max_length=100)
