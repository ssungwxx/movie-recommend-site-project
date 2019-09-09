from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Rating
from api.serializers import RatingSerializer
from rest_framework.response import Response
from django.db.models import Avg


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def ratings(request):

    if request.method == 'GET':
        movieid = request.GET.get('movieid', None)

        ratings = Rating.objects.all()

        if movieid:
            ratings = ratings.filter(movieid=movieid)

        serializer = RatingSerializer(ratings, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        rating = Rating.objects.all()
        rating.delete()
        return Response(status=status.HTTP_200_OK)

    if request.method == 'POST':
        ratings = request.data.get('ratings', None)
        for item in ratings:
            userid = item.get('userid', None)
            movieid = item.get('movieid', None)
            rating = item.get('rating', None)
            timestamp = item.get('timestamp', None)

            if not (userid and movieid and rating and timestamp):
                continue

            Rating(userid_id=userid,
                   movieid_id=movieid,
                   rating=rating,
                   timestamp=timestamp).save()

        return Response(status=status.HTTP_200_OK)\

    if request.method == 'PUT':
        rating = Rating.objects.get(id=request.data.get('id'))

        serializer = RatingSerializer(rating, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
