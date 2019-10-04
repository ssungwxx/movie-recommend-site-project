
# Item_based Collaborative Filtering



import numpy as np 
import pandas as pd
from sklearn.metrics import pairwise_distances


def main():
    users = pd.read_csv("users.csv", encoding="latin-1")
    movies = pd.read_csv("movies.csv", encoding="latin-1")
    ratings = pd.read_csv("ratings.csv", encoding="latin-1")
    movie_ratings = pd.merge(movies, ratings)
    df = pd.merge(movie_ratings, users)
    df.drop(df.columns[[5,9]], axis=1, inplace=True)
    ratings.drop( "timestamp", inplace = True, axis = 1 )

    movie_stats = df.groupby('movie_id').agg({'rating': [np.size, np.mean]})


    min_30 = movie_stats['rating']['size'] >= 30

    ratings_matrix = ratings.pivot_table(index=['movie_id'], columns=['user_id'], values='rating').reset_index(drop=False)
    ratings_matrix2 = ratings.pivot_table(index=['movie_id'], columns=['user_id'], values='rating').reset_index(drop=False)


    ratings_matrix.fillna( 0, inplace=True)
    ratings_matrix2.fillna( 0, inplace=True)


    movie_similarity = 1 - pairwise_distances( ratings_matrix.as_matrix(), metric='cosine' )
    np.fill_diagonal( movie_similarity, 0 ) #Filling diagonals with 0s for future use when sorting is done
    ratings_matrix = pd.DataFrame( movie_similarity )
    movies.drop("genres", inplace=True, axis = 1)

    size = movies.index.size
    preprocessing_data = np.zeros((size, 6))
    idx = 0
    for item in movies['movie_id']:

        user_inp = item
        preprocessing_data[idx, 0] = item
        try:
            inp = ratings_matrix2[ratings_matrix2['movie_id'] == user_inp].index.tolist()
            inp = inp[0]

            movies['similarity'] = ratings_matrix.iloc[inp]
            movies.columns = ['movie_id', 'movie', 'similarity']
            sort_movies = movies.sort_values(['similarity'], ascending=False)
            cnt = 1
            for i in sort_movies.movie_id[0:5]:
                preprocessing_data[idx, cnt] = i
                cnt = cnt + 1

        except:
            preprocessing_data[idx, 1] = -1
        idx = idx + 1

    preprocessing_data = preprocessing_data.astype(int)
    preprocessing_data
    np.savetxt('item_based_KNN.dat', preprocessing_data, delimiter='::', fmt='%d')  # array data를 .dat 파일로 변환시켜서 저장



if __name__ == '__main__':
    main()

