
from rest_framework import status
from rest_framework.decorators import api_view
from api.models import item_based_movie
from api.serializers import Recommend_movieSerializer
from rest_framework.response import Response
from django.db.models import Avg


@api_view(['GET','POST'])
def item_based_movies(request):
    if request.method == 'GET':
        id = request.GET.get('id', request.GET.get('movieid', None))
        movies = item_based_movies.objects.all()
        # 해당 id에 대한 추천 movieid를 필터링해서 가져옴
        if id:
            movies = movies.filter(pk=id)
    
        serializer = Recommend_movieSerializer(movies, many=True) # <-- 수정해야함

        print("----------------------")
        return Response(data=serializer.data, status=status.HTTP_200_OK)



    if request.method == 'POST':
        item_based_movies = request.data.get('item_based', None)
        print(item_based_movies)
        for item in item_based_movies:
            movieid = item.get('movieid',None)
            rank1 = item.get('rank1', None)
            rank2 = item.get('rank2', None)
            rank3 = item.get('rank3', None)
            rank4 = item.get('rank4', None)
            rank5 = item.get('rank5', None)
            
            item_based_movie(movieid = movieid,
                   rank1 = rank1,
                   rank2 = rank2,
                   rank3 = rank3,
                   rank4 = rank4,
                   rank5 = rank5).save()
        return Response(status=status.HTTP_200_OK)
