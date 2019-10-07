from rest_framework import status
from rest_framework.decorators import api_view
from api.models import movie_url
from api.serializers import MovieurlSerializer
from rest_framework.response import Response
from django.db.models import Avg


@api_view(['GET','POST'])
def movie_urls(request):
    if request.method == 'GET':
        id = request.GET.get('id', request.GET.get('movieid', None))
        movies = movie_url.objects.all()
        # 해당 id에 대한 추천 movieid를 필터링해서 가져옴
        if id:
            movies = movies.filter(pk=id)
    
        serializer = MovieurlSerializer(movies, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)



    if request.method == 'POST':
        movie_urls = request.data.get('movie_urls', None)
        for item in movie_urls:
            movieid = item.get('movieid',None)
            url = item.get('url', None)

            movie_url(movieid = movieid,
                   url = url).save()

        return Response(status=status.HTTP_200_OK)
