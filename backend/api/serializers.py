# -*- coding:utf-8 -*-
from .models import Profile, Movie, Rating, Like_movie
from rest_framework import serializers
from django.db.models import Avg


class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    username = serializers.SerializerMethodField('get_username')
    is_staff = serializers.SerializerMethodField('get_is_staff')

    class Meta:
        model = Profile
        fields = ('id', 'username', 'is_staff', 'gender', 'age', 'occupation')

    def get_username(self, obj):
        return obj.user.username

    def get_is_staff(self, obj):
        return obj.user.is_staff


class MovieSerializer(serializers.ModelSerializer):
    genres_array = serializers.ReadOnlyField()
    average_rating = serializers.SerializerMethodField('get_average_rating')
    view_cnt = serializers.SerializerMethodField('get_view_cnt')

    class Meta:
        model = Movie
        fields = ('id', 'title', 'genres_array', 'view_cnt',
                  'average_rating')

    def get_average_rating(self, obj):
        total = 0
        for item in obj.ratings.values():
            total += item.get('rating')
        if obj.ratings.count() > 0:
            return round(int(total) / obj.ratings.count(), 1)

        return 0

    def get_view_cnt(self, obj):
        return obj.ratings.count()

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.title = validated_data.get('title', instance.title)
        instance.genres = validated_data.get('genres', instance.genres)
        instance.save()
        return instance


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'userid', 'movieid', 'rating', 'timestamp')



class Like_movieSerializer(serializers.ModelSerializer):
    recommend_list_id = serializers.SerializerMethodField('get_recommend_list_id')
    recommend_list_title = serializers.SerializerMethodField('get_recommend_list_title')


    class Meta:
        model = Like_movie
        fields = ('movieid', 'recommend_list_id', 'recommend_list_title')
    
    def get_recommend_list_id(self, obj):
        recommend_list_id = (obj.rank1, obj.rank2, obj.rank3, obj.rank4, obj.rank5, obj.rank6, obj.rank7, obj.rank8, obj.rank9, obj.rank10)

        return recommend_list_id

    def get_recommend_list_title(self, obj):
        recommend_list_title = [obj.rank1, obj.rank2, obj.rank3, obj.rank4, obj.rank5, obj.rank6, obj.rank7, obj.rank8, obj.rank9, obj.rank10]
        idx = 0

        for item in recommend_list_title:
            movie = Movie.objects.all()
            movie = movie.filter(pk=item)
            recommend_list_title[idx] = movie[0].title
            idx = idx + 1

        return recommend_list_title
        
        