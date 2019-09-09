from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Movie
from api.models import Rating
from api.serializers import MovieSerializer
from api.serializers import RatingSerializer
from rest_framework.response import Response


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def movies(request):

    if request.method == 'GET':
        id = request.GET.get('id', request.GET.get('movie_id', None))
        title = request.GET.get('title', None)
        genre = request.GET.get('genre', None)

        movies = Movie.objects.all()

        if id:
            movies = movies.filter(pk=id)
        if title:
            movies = movies.filter(title__icontains=title)
        if genre:
            movies = movies.filter(genres__icontains=genre)

        serializer = MovieSerializer(movies, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        movie = Movie.objects.all()
        movie.delete()
        return Response(status=status.HTTP_200_OK)

    if request.method == 'POST':
        movies = request.data.get('movies', None)
        for movie in movies:
            id = movie.get('id', None)
            title = movie.get('title', None)
            genres = movie.get('genres', None)

            if not (id and title and genres):
                continue
            if Movie.objects.filter(id=id).count() > 0 or Movie.objects.filter(
                    title=title).count() > 0:
                continue

            Movie(id=id, title=title, genres='|'.join(genres)).save()

        return Response(status=status.HTTP_200_OK)

    if request.method == 'PUT':
        movie = Movie.objects.get(id=request.data.get('id'))

        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.update(movie, request.data)
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
