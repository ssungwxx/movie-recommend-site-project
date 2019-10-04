

```python
# Item_based Collaborative Filtering
```


```python
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.metrics import pairwise_distances
from scipy.spatial.distance import cosine, correlation
```


```python
users = pd.read_csv("users.csv", encoding="latin-1")
movies = pd.read_csv("movies.csv", encoding="latin-1")
ratings = pd.read_csv("ratings.csv", encoding="latin-1")
```


```python
movie_ratings = pd.merge(movies, ratings)
df = pd.merge(movie_ratings, users)
```


```python
df.drop(df.columns[[5,9]], axis=1, inplace=True)
ratings.drop( "timestamp", inplace = True, axis = 1 )
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 1000209 entries, 0 to 1000208
    Data columns (total 8 columns):
    movie_id      1000209 non-null int64
    movie         1000209 non-null object
    genres        1000209 non-null object
    user_id       1000209 non-null int64
    rating        1000209 non-null int64
    gender        1000209 non-null object
    age           1000209 non-null object
    occupation    1000209 non-null object
    dtypes: int64(3), object(5)
    memory usage: 68.7+ MB
    


```python
movie_stats = df.groupby('movie_id').agg({'rating': [np.size, np.mean]})
movie_stats.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="2" halign="left">rating</th>
    </tr>
    <tr>
      <th></th>
      <th>size</th>
      <th>mean</th>
    </tr>
    <tr>
      <th>movie_id</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>2077</td>
      <td>4.146846</td>
    </tr>
    <tr>
      <th>2</th>
      <td>701</td>
      <td>3.201141</td>
    </tr>
    <tr>
      <th>3</th>
      <td>478</td>
      <td>3.016736</td>
    </tr>
    <tr>
      <th>4</th>
      <td>170</td>
      <td>2.729412</td>
    </tr>
    <tr>
      <th>5</th>
      <td>296</td>
      <td>3.006757</td>
    </tr>
  </tbody>
</table>
</div>




```python
min_30 = movie_stats['rating']['size'] >= 30
movie_stats[min_30].sort_values([('rating','mean')], ascending=False).head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="2" halign="left">rating</th>
    </tr>
    <tr>
      <th></th>
      <th>size</th>
      <th>mean</th>
    </tr>
    <tr>
      <th>movie_id</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2905</th>
      <td>69</td>
      <td>4.608696</td>
    </tr>
    <tr>
      <th>2019</th>
      <td>628</td>
      <td>4.560510</td>
    </tr>
    <tr>
      <th>318</th>
      <td>2227</td>
      <td>4.554558</td>
    </tr>
    <tr>
      <th>858</th>
      <td>2223</td>
      <td>4.524966</td>
    </tr>
    <tr>
      <th>745</th>
      <td>657</td>
      <td>4.520548</td>
    </tr>
  </tbody>
</table>
</div>




```python
ratings_matrix = ratings.pivot_table(index=['movie_id'], columns=['user_id'], values='rating').reset_index(drop=False)
ratings_matrix2 = ratings.pivot_table(index=['movie_id'], columns=['user_id'], values='rating').reset_index(drop=False)

```


```python
ratings_matrix.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>user_id</th>
      <th>movie_id</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>...</th>
      <th>6031</th>
      <th>6032</th>
      <th>6033</th>
      <th>6034</th>
      <th>6035</th>
      <th>6036</th>
      <th>6037</th>
      <th>6038</th>
      <th>6039</th>
      <th>6040</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>5.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4.0</td>
      <td>NaN</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>4.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 6041 columns</p>
</div>




```python
ratings_matrix.fillna( 0, inplace=True)
ratings_matrix2.fillna( 0, inplace=True)
ratings_matrix2.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>user_id</th>
      <th>movie_id</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>...</th>
      <th>6031</th>
      <th>6032</th>
      <th>6033</th>
      <th>6034</th>
      <th>6035</th>
      <th>6036</th>
      <th>6037</th>
      <th>6038</th>
      <th>6039</th>
      <th>6040</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>4.0</td>
      <td>0.0</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>4.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>4.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 6041 columns</p>
</div>




```python
movie_similarity = 1 - pairwise_distances( ratings_matrix.as_matrix(), metric='cosine' )
np.fill_diagonal( movie_similarity, 0 ) #Filling diagonals with 0s for future use when sorting is done
ratings_matrix = pd.DataFrame( movie_similarity )
```

    C:\ProgramData\Anaconda3\lib\site-packages\ipykernel_launcher.py:1: FutureWarning: Method .as_matrix will be removed in a future version. Use .values instead.
      """Entry point for launching an IPython kernel.
    


```python
# Recommender Engine


movies.drop("genres", inplace=True, axis = 1)
```


```python
try:
    movie_input = int(input("영화 아이디 입력 : "))

    user_inp= movie_input
    inp=ratings_matrix2[ratings_matrix2['movie_id']==user_inp].index.tolist()
    print(inp[0])
    inp=inp[0]

    movies['similarity'] = ratings_matrix.iloc[inp]
    movies.columns = ['movie_id', 'movie','similarity']
    sort_movies = movies.sort_values(['similarity'], ascending=False)

    print(" ")
    print("--------------------------------추천영화-----------")
    for i in sort_movies.movie_id[0:5]:
        print(i)

except:
    print("평점없음")
```

    영화 아이디 입력 : 3
    2
     
    --------------------------------추천영화-----------
    991
    1065
    1539
    1192
    423
    


```python
#print("Recommended movies based on your choice of ",user_inp ,": \n", movies.sort_values( ["similarity"], ascending = False )[0:10])
```


```python
%%time
size = movies.index.size
preprocessing_data = np.zeros((size,6))
idx = 0
for item in movies['movie_id']:
    
    user_inp=item
    preprocessing_data[idx,0] = item
    try:
        inp=ratings_matrix2[ratings_matrix2['movie_id']==user_inp].index.tolist()
        inp=inp[0]

        movies['similarity'] = ratings_matrix.iloc[inp]
        movies.columns = ['movie_id', 'movie','similarity']
        sort_movies = movies.sort_values(['similarity'], ascending=False)
        cnt = 1
        for i in sort_movies.movie_id[0:5]:
            preprocessing_data[idx,cnt] = i
            cnt = cnt+1
    
    except:
        preprocessing_data[idx,1] = -1
    idx = idx + 1
```

    Wall time: 20.4 s
    


```python
preprocessing_data = preprocessing_data.astype(int)
preprocessing_data
```




    array([[   1,    2, 1326, 1346, 3010, 1353],
           [   2,   11,  808, 1096, 3560, 1810],
           [   3,  991, 1065, 1539, 1192,  423],
           ...,
           [3950, 2313, 1946, 1450, 1906,  628],
           [3951,  175,  873, 1286,  197, 1508],
           [3952,  965, 2341,  934, 2247, 1911]])




```python
np.savetxt('item_based_KNN.dat', preprocessing_data, delimiter='::', fmt='%d')  # array data를 .dat 파일로 변환시켜서 저장
```


```python

```
