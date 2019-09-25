

# Collaborative filtering



```python
import numpy as np
import pandas as pd

ratings_data = pd.read_csv("ratings.csv", encoding='utf-8')
movie_names = pd.read_csv("movies.csv", encoding='iso-8859-1')
movie_data = pd.merge(ratings_data, movie_names, on="movie_id")

# ratings.csv ,, movies.csv 파일을 불러와서 merge시켜 movie_data를 생성


ratings_mean_count = pd.DataFrame(movie_data.groupby('movie_id')['rating'].mean())

ratings_mean_count['rating_counts'] = pd.DataFrame(movie_data.groupby('movie_id')['rating'].count())

user_movie_rating = movie_data.pivot_table(index="user_id", columns='movie_id', values='rating')

movie_id = 0;
size = user_movie_rating.columns.size
preprocessing_data = np.zeros((size,31))



for item in user_movie_rating.columns:
    print(item)
    preprocessing_data[movie_id,0] = item
    item_ratings = user_movie_rating[item]
    movies_like_item = user_movie_rating.corrwith(item_ratings)
    
    corr_item = pd.DataFrame(movies_like_item, columns=['Correlation'])
    corr_item.dropna(inplace=True)
    corr_item.sort_values('Correlation', ascending=False, inplace=True)
    corr_movie_id = 1
    
    
    for i in corr_item.index[0:30]:
        if item != i:
            preprocessing_data[movie_id,corr_movie_id] = int(i)
            corr_movie_id = corr_movie_id+1
    
    movie_id = movie_id+1
    


preprocessing_data = preprocessing_data.astype(int) # 형변환시킴
np.savetxt('like_movie_version1.1.dat', preprocessing_data, delimiter='::', fmt='%d')  # array data를 .dat 파일로 변환시켜서 저장

```



like_movie_version1.1.dat 

 3706 x 30 개로 

 첫번째 열은 해당 movie_id

 2번째~30번째  유사한 영화를 sort시켜서 저장시킴 2번째일수록 유사도가 높음