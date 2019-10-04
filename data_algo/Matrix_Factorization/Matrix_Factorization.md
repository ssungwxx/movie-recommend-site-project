

```python
import pandas as pd
import numpy as np

movies = pd.read_csv("movies.csv", encoding = "latin-1")
ratings = pd.read_csv("ratings.csv", encoding = "latin-1")
```


```python
combine_movie_rating = pd.merge(ratings, movies, on="movie_id")
```


```python
columns = ['timestamp', 'genres']
combine_movie_rating = combine_movie_rating.drop(columns, axis = 1)
combine_movie_rating.head()
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
      <th></th>
      <th>user_id</th>
      <th>movie_id</th>
      <th>rating</th>
      <th>movie</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1193</td>
      <td>5</td>
      <td>One Flew Over the Cuckoo's Nest (1975)</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1193</td>
      <td>5</td>
      <td>One Flew Over the Cuckoo's Nest (1975)</td>
    </tr>
    <tr>
      <th>2</th>
      <td>12</td>
      <td>1193</td>
      <td>4</td>
      <td>One Flew Over the Cuckoo's Nest (1975)</td>
    </tr>
    <tr>
      <th>3</th>
      <td>15</td>
      <td>1193</td>
      <td>4</td>
      <td>One Flew Over the Cuckoo's Nest (1975)</td>
    </tr>
    <tr>
      <th>4</th>
      <td>17</td>
      <td>1193</td>
      <td>5</td>
      <td>One Flew Over the Cuckoo's Nest (1975)</td>
    </tr>
  </tbody>
</table>
</div>




```python
combine_movie_rating = combine_movie_rating.dropna(axis = 0, subset = ['movie_id'])
movie_ratingCount = (combine_movie_rating.groupby(by = ['movie_id'])['rating'].count().reset_index().rename(columns = {'rating': 'totalRatingCount'})[['movie_id', 'totalRatingCount']])

```


```python
rating_with_totalRatingCount = combine_movie_rating.merge(movie_ratingCount, left_on = 'movie_id', right_on = 'movie_id', how = 'left')
rating_with_totalRatingCount.head()
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
      <th></th>
      <th>user_id</th>
      <th>movie_id</th>
      <th>rating</th>
      <th>movie</th>
      <th>totalRatingCount</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1193</td>
      <td>5</td>
      <td>One Flew Over the Cuckoo's Nest (1975)</td>
      <td>1725</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1193</td>
      <td>5</td>
      <td>One Flew Over the Cuckoo's Nest (1975)</td>
      <td>1725</td>
    </tr>
    <tr>
      <th>2</th>
      <td>12</td>
      <td>1193</td>
      <td>4</td>
      <td>One Flew Over the Cuckoo's Nest (1975)</td>
      <td>1725</td>
    </tr>
    <tr>
      <th>3</th>
      <td>15</td>
      <td>1193</td>
      <td>4</td>
      <td>One Flew Over the Cuckoo's Nest (1975)</td>
      <td>1725</td>
    </tr>
    <tr>
      <th>4</th>
      <td>17</td>
      <td>1193</td>
      <td>5</td>
      <td>One Flew Over the Cuckoo's Nest (1975)</td>
      <td>1725</td>
    </tr>
  </tbody>
</table>
</div>




```python
user_rating = rating_with_totalRatingCount.drop_duplicates(['user_id','movie'])
user_rating.head()
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
      <th></th>
      <th>user_id</th>
      <th>movie_id</th>
      <th>rating</th>
      <th>movie</th>
      <th>totalRatingCount</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1193</td>
      <td>5</td>
      <td>One Flew Over the Cuckoo's Nest (1975)</td>
      <td>1725</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1193</td>
      <td>5</td>
      <td>One Flew Over the Cuckoo's Nest (1975)</td>
      <td>1725</td>
    </tr>
    <tr>
      <th>2</th>
      <td>12</td>
      <td>1193</td>
      <td>4</td>
      <td>One Flew Over the Cuckoo's Nest (1975)</td>
      <td>1725</td>
    </tr>
    <tr>
      <th>3</th>
      <td>15</td>
      <td>1193</td>
      <td>4</td>
      <td>One Flew Over the Cuckoo's Nest (1975)</td>
      <td>1725</td>
    </tr>
    <tr>
      <th>4</th>
      <td>17</td>
      <td>1193</td>
      <td>5</td>
      <td>One Flew Over the Cuckoo's Nest (1975)</td>
      <td>1725</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Matrix Factorization
```


```python
movie_user_rating_pivot = user_rating.pivot(index='user_id', columns = 'movie_id', values = 'rating').fillna(0)
movie_user_rating_pivot.head()
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
      <th>10</th>
      <th>...</th>
      <th>3943</th>
      <th>3944</th>
      <th>3945</th>
      <th>3946</th>
      <th>3947</th>
      <th>3948</th>
      <th>3949</th>
      <th>3950</th>
      <th>3951</th>
      <th>3952</th>
    </tr>
    <tr>
      <th>user_id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>5.0</td>
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
      <th>3</th>
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
      <th>4</th>
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
      <th>5</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2.0</td>
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
  </tbody>
</table>
<p>5 rows × 3706 columns</p>
</div>




```python
X = movie_user_rating_pivot.values.T
```


```python
import sklearn
from sklearn.decomposition import TruncatedSVD

SVD = TruncatedSVD(n_components = 12, random_state = 17)
matrix = SVD.fit_transform(X)
```


```python
corr = np.corrcoef(matrix)
```


```python
movie_title = movie_user_rating_pivot.columns
movie_title_list = list(movie_title)
```


```python
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
```


```python
preprocessing_data = preprocessing_data.astype(int)
np.savetxt('Maxtrix_Factorization.dat', preprocessing_data, delimiter='::', fmt='%d')  # array data를 .dat 파일로 변환시켜서 저장
```


```python

```
