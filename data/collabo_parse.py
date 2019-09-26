# -*- coding:utf-8 -*-

import requests
import json

API_URL = 'http://localhost:8000/api/'
headers = {'content-type': 'application/json'}


def create_like_movie():
    like_movie_data = open('./like_movie_version1.1.dat', 'r', encoding='ISO-8859-1')
    request_data = {'like_movies': []}

    for line in like_movie_data.readlines():
        [movieid, rank1, rank2, rank3, rank4, rank5, rank6, rank7, rank8, rank9, rank10, rank11, rank12, rank13, rank14, rank15, rank16, rank17, rank18, rank19, rank20, rank21, rank22, rank23, rank24, rank25, rank26, rank27, rank28, rank29, rank30] = line.split('::')
           
        
        request_data['like_movies'].append({
            'movieid': movieid,
            'rank1': rank1,
            'rank2': rank2,
            'rank3': rank3,
            'rank4': rank4,
            'rank5': rank5,
            'rank6': rank6,
            'rank7': rank7,
            'rank8': rank8,
            'rank9': rank9,
            'rank10': rank10
        })


        
    print("like_movie 넣는중")
    response = requests.post(API_URL + 'likemovie/',
                             data=json.dumps(request_data),
                             headers=headers)
    # print(response.text)




if __name__ == '__main__':
    create_like_movie()
