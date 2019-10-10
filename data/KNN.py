# -*- coding:utf-8 -*-

import requests
import json

API_URL = 'http://localhost:8000/api/'
headers = {'content-type': 'application/json'}


def create_item_based():
    item_based = open('./item_based_KNN.dat', 'r', encoding='ISO-8859-1')
    request_data = {'item_based': []}

    for line in item_based.readlines():
        [movieid, rank1, rank2, rank3, rank4, rank5] = line.split('::')
           
        
        request_data['item_based'].append({
            'movieid': movieid,
            'rank1': rank1,
            'rank2': rank2,
            'rank3': rank3,
            'rank4': rank4,
            'rank5': rank5
        })


        
    print("item_based 넣는중")
    response = requests.post(API_URL + 'itembased/',
                             data=json.dumps(request_data),
                             headers=headers)
    # print(response.text)

def create_user_based():
    user_based = open('./user_based_KNN.dat', 'r', encoding='ISO-8859-1')
    request_data = {'user_based': []}

    for line in user_based.readlines():
        [movieid, rank1, rank2, rank3, rank4, rank5] = line.split('::')
        
        request_data['user_based'].append({
            'movieid': movieid,
            'rank1': rank1,
            'rank2': rank2,
            'rank3': rank3,
            'rank4': rank4,
            'rank5': rank5
        })


        
    print("user_item 넣는중")
    response = requests.post(API_URL + 'userbased/',
                             data=json.dumps(request_data),
                             headers=headers)
    # print(response.text)


def create_matrix_factorization():
    matrix_factorization = open('./Matrix_Factorization.dat', 'r', encoding='ISO-8859-1')
    request_data = {'matrix_factorization': []}

    for line in matrix_factorization.readlines():
        [movieid, rank1, rank2, rank3, rank4, rank5] = line.split('::')
           
        
        request_data['matrix_factorization'].append({
            'movieid': movieid,
            'rank1': rank1,
            'rank2': rank2,
            'rank3': rank3,
            'rank4': rank4,
            'rank5': rank5
        })


        
    print("matrix_factorization 넣는중")
    response = requests.post(API_URL + 'matrixfactorization/',
                             data=json.dumps(request_data),
                             headers=headers)
    # print(response.text)
if __name__ == '__main__':
    create_item_based()
    create_user_based()
    create_matrix_factorization()