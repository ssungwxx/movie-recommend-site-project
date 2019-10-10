from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Profile
from api.serializers import ProfileSerializer
from rest_framework.response import Response
from api.models import create_profile


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def profiles(request):

    if request.method == 'GET':
        userid = title = request.GET.get('id', None)

        profiles = Profile.objects.all()

        if userid:
            profiles = profiles.filter(pk=userid)

        serializer = ProfileSerializer(profiles, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        profile = Profile.objects.get(id=request.data.get('id'))

        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.update(profile, request.data)
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':
        profile = request.data.get('params')
        print(profile)
        username = profile.get('User')
        age = profile.get('Age')
        occupation = profile.get('Occupation')
        gender = profile.get('Gender')

        create_profile(username=username,
                       age=age,
                       occupation=occupation,
                       gender=gender)

        return Response(status=status.HTTP_201_CREATED)
