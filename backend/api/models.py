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