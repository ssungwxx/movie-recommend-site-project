from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Movie
from api.models import Rating, Profile
from api.serializers import MovieSerializer, RatingSerializer, ProfileSerializer
from rest_framework.response import Response
import operator


@api_view(['GET'])
def classify_movies(req):
    if req.method == 'GET':
        gender = req.GET.get('gender', None)
        age = req.GET.get('age', None)
        occupation = req.GET.get('occupation', None)

        movies = Movie.objects.all()
        ratings = Rating.objects.all()
        profiles = Profile.objects.all()
        result = []

        if gender:
            if gender == '남':
                gender = 'M'
            else:
                gender = 'F'
            for movie in movies:
                count = 0
                movie_ratings = ratings.filter(movieid=movie.id)
                if movie_ratings.count() is not 0:
                    for rating in movie_ratings:
                        user = profiles.filter(user_id=rating.userid)

                        if user[0].gender == gender:
                            count += 1
                    if count > (movie_ratings.count()/2):
                        result.append(movie)

        if age:
            for movie in movies:
                count = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
                movie_ratings = ratings.filter(movieid=movie.id)
                if movie_ratings.count() is not 0:
                    for rating in movie_ratings:
                        user = profiles.filter(user_id=rating.userid)
                        tmp = user[0].age // 10
                        count[tmp] += 1

                    sorted_count = sorted(
                        count.items(), key=operator.itemgetter(1), reverse=True)

                    if int(age) // 10 == sorted_count[0][0]:
                        result.append(movie)

        if occupation:
            occupation_map = {
                'other': 0,
                'academic': 1,
                'educator': 1,
                'artist': 2,
                'clerical': 3,
                'admin': 3,
                'college': 4,
                'grad student': 4,
                'customer service': 5,
                'doctor': 6,
                'health care': 6,
                'executive': 7,
                'managerial': 7,
                'farmer': 8,
                'homemaker': 9,
                'K-12 student': 10,
                'lawyer': 11,
                'programmer': 12,
                'retured': 13,
                'sales': 14,
                'marketing': 14,
                'scientist': 15,
                'self-employed': 16,
                'technician': 17,
                'engineer': 17,
                'tradesman': 18,
                'craftsman':  18,
                'unemployed': 19,
                'writer': 20
            }

            for movie in movies:
                count = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0,
                         11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0}
                movie_ratings = ratings.filter(movieid=movie.id)
                if movie_ratings.count() is not 0:
                    for rating in movie_ratings:
                        user = profiles.filter(user_id=rating.userid)
                        user_occ = occupation_map[user[0].occupation]
                        count[user_occ] += 1

                    sorted_count = sorted(
                        count.items(), key=operator.itemgetter(1), reverse=True)

                    if int(occupation) == sorted_count[0][0]:
                        result.append(movie)

        serializer = MovieSerializer(result, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
