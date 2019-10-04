import pandas as pd
import numpy as np
import sklearn
from sklearn.decomposition import TruncatedSVD


def main():
    movies = pd.read_csv("movies.csv", encoding = "latin-1")
    ratings = pd.read_csv("ratings.csv", encoding = "latin-1")
    combine_movie_rating = pd.merge(ratings, movies, on="movie_id")

    columns = ['timestamp', 'genres']
    combine_movie_rating = combine_movie_rating.drop(columns, axis = 1)
    combine_movie_rating = combine_movie_rating.dropna(axis = 0, subset = ['movie_id'])
    movie_ratingCount = (combine_movie_rating.groupby(by = ['movie_id'])['rating'].count().reset_index().rename(columns = {'rating': 'totalRatingCount'})[['movie_id', 'totalRatingCount']])

    rating_with_totalRatingCount = combine_movie_rating.merge(movie_ratingCount, left_on = 'movie_id', right_on = 'movie_id', how = 'left')


    user_rating = rating_with_totalRatingCount.drop_duplicates(['user_id','movie'])


    movie_user_rating_pivot = user_rating.pivot(index='user_id', columns = 'movie_id', values = 'rating').fillna(0)
    X = movie_user_rating_pivot.values.T
    SVD = TruncatedSVD(n_components = 12, random_state = 17)
    matrix = SVD.fit_transform(X)
    corr = np.corrcoef(matrix)


    movie_title = movie_user_rating_pivot.columns
    movie_title_list = list(movie_title)


    size = movies.index.size
    preprocessing_data = np.zeros((size,6))
    idx = 0
    for item in movies['movie_id']:
        movieid = item
        try:
            coffey_hands = movie_title_list.index(item)
            preprocessing_data[idx,0] = item
            corr_coffey_hands = corr[coffey_hands]
            like_movie = list(movie_title[(corr_coffey_hands >= 0.9)])
            cnt = 1
            for i in like_movie:
                preprocessing_data[idx,cnt] = i
                if i==item:
                    continue
                cnt = cnt+1
                if cnt == 6:
                    break
        except:
            preprocessing_data[idx,0] = item
            preprocessing_data[idx,1] = -1
        idx = idx + 1

    preprocessing_data = preprocessing_data.astype(int)
    np.savetxt('Matrix_Factorization.dat', preprocessing_data, delimiter='::', fmt='%d')  # array data를 .dat 파일로 변환시켜서 저장


if __name__ == '__main__':
    main()


