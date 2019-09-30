

```python
# 유저간의 유사도를 이용하여 영화 추천 해주는 KNN 
# user_based

```


```python
import pandas as pd
import numpy as np
from sklearn.metrics import pairwise_distances
```


```python
movies = pd.read_csv("movies.csv",encoding="Latin1")
Ratings = pd.read_csv("ratings.csv")
```


```python
movies.head()
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
      <th>movie_id</th>
      <th>movie</th>
      <th>genres</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Toy Story (1995)</td>
      <td>Animation|Children's|Comedy</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Jumanji (1995)</td>
      <td>Adventure|Children's|Fantasy</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Grumpier Old Men (1995)</td>
      <td>Comedy|Romance</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Waiting to Exhale (1995)</td>
      <td>Comedy|Drama</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Father of the Bride Part II (1995)</td>
      <td>Comedy</td>
    </tr>
  </tbody>
</table>
</div>




```python
Mean = Ratings.groupby(by="user_id",as_index=False)['rating'].mean()
Rating_avg = pd.merge(Ratings,Mean,on='user_id')
Rating_avg['adg_rating']=Rating_avg['rating_x']-Rating_avg['rating_y']
Rating_avg.head()
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
      <th>rating_x</th>
      <th>timestamp</th>
      <th>rating_y</th>
      <th>adg_rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1193</td>
      <td>5</td>
      <td>978300760</td>
      <td>4.188679</td>
      <td>0.811321</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>661</td>
      <td>3</td>
      <td>978302109</td>
      <td>4.188679</td>
      <td>-1.188679</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>914</td>
      <td>3</td>
      <td>978301968</td>
      <td>4.188679</td>
      <td>-1.188679</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>3408</td>
      <td>4</td>
      <td>978300275</td>
      <td>4.188679</td>
      <td>-0.188679</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>2355</td>
      <td>5</td>
      <td>978824291</td>
      <td>4.188679</td>
      <td>0.811321</td>
    </tr>
  </tbody>
</table>
</div>




```python
check = pd.pivot_table(Rating_avg,values='rating_x',index='user_id',columns='movie_id')
check.head()
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
      <th>3</th>
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
      <th>4</th>
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
      <th>5</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.0</td>
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
  </tbody>
</table>
<p>5 rows × 3706 columns</p>
</div>




```python
# use cosine similarity
from sklearn.metrics.pairwise import cosine_similarity

# sklearn에서 제공해주는 cosine_similarity 사용 
# 명세서에서 user_based KNN 구현하기위해서 sklearn의 라이브러리 사용 가능

```


```python
final = pd.pivot_table(Rating_avg,values='adg_rating', index='user_id', columns='movie_id')
# index -> user_id로 지정하고 columns는 movie_id로 지정한 후 
# 해당값은 adg_rating의 값이 들어감
```


```python
final_movie = final.fillna(final.mean(axis=0))

# Nan의 값은 평균값으로 채워넣는 과정

# 총 2가지 방법이 존재
# 1. 유저기준으로 평균값으로 채움
# 2. 영화기준으로 평균값으로 채움

# 여기서는 영화 기준으로 평균값을 채울거임

# user Avg 도 똑같이 
final_user = final.apply(lambda row: row.fillna(row.mean()), axis=1)
```


```python
final_movie.head()
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
      <td>0.811321</td>
      <td>-0.324143</td>
      <td>-0.440247</td>
      <td>-0.698816</td>
      <td>-0.419777</td>
      <td>0.280853</td>
      <td>-0.11491</td>
      <td>-0.443714</td>
      <td>-0.725926</td>
      <td>0.000378</td>
      <td>...</td>
      <td>-0.41009</td>
      <td>-1.175689</td>
      <td>-1.844868</td>
      <td>-1.228738</td>
      <td>-0.084698</td>
      <td>0.027156</td>
      <td>0.549132</td>
      <td>0.052553</td>
      <td>0.356937</td>
      <td>0.165338</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.479497</td>
      <td>-0.324143</td>
      <td>-0.440247</td>
      <td>-0.698816</td>
      <td>-0.419777</td>
      <td>0.280853</td>
      <td>-0.11491</td>
      <td>-0.443714</td>
      <td>-0.725926</td>
      <td>0.000378</td>
      <td>...</td>
      <td>-0.41009</td>
      <td>-1.175689</td>
      <td>-1.844868</td>
      <td>-1.228738</td>
      <td>-0.084698</td>
      <td>0.027156</td>
      <td>0.549132</td>
      <td>0.052553</td>
      <td>0.356937</td>
      <td>0.165338</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.479497</td>
      <td>-0.324143</td>
      <td>-0.440247</td>
      <td>-0.698816</td>
      <td>-0.419777</td>
      <td>0.280853</td>
      <td>-0.11491</td>
      <td>-0.443714</td>
      <td>-0.725926</td>
      <td>0.000378</td>
      <td>...</td>
      <td>-0.41009</td>
      <td>-1.175689</td>
      <td>-1.844868</td>
      <td>-1.228738</td>
      <td>-0.084698</td>
      <td>0.027156</td>
      <td>0.549132</td>
      <td>0.052553</td>
      <td>0.356937</td>
      <td>0.165338</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.479497</td>
      <td>-0.324143</td>
      <td>-0.440247</td>
      <td>-0.698816</td>
      <td>-0.419777</td>
      <td>0.280853</td>
      <td>-0.11491</td>
      <td>-0.443714</td>
      <td>-0.725926</td>
      <td>0.000378</td>
      <td>...</td>
      <td>-0.41009</td>
      <td>-1.175689</td>
      <td>-1.844868</td>
      <td>-1.228738</td>
      <td>-0.084698</td>
      <td>0.027156</td>
      <td>0.549132</td>
      <td>0.052553</td>
      <td>0.356937</td>
      <td>0.165338</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.479497</td>
      <td>-0.324143</td>
      <td>-0.440247</td>
      <td>-0.698816</td>
      <td>-0.419777</td>
      <td>-1.146465</td>
      <td>-0.11491</td>
      <td>-0.443714</td>
      <td>-0.725926</td>
      <td>0.000378</td>
      <td>...</td>
      <td>-0.41009</td>
      <td>-1.175689</td>
      <td>-1.844868</td>
      <td>-1.228738</td>
      <td>-0.084698</td>
      <td>0.027156</td>
      <td>0.549132</td>
      <td>0.052553</td>
      <td>0.356937</td>
      <td>0.165338</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 3706 columns</p>
</div>




```python
b = cosine_similarity(final_user)
np.fill_diagonal(b, 0 )
similarity_with_user = pd.DataFrame(b,index=final_user.index)
similarity_with_user.columns=final_user.index
similarity_with_user.head()
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
      <td>0.000000</td>
      <td>0.032665</td>
      <td>-0.032267</td>
      <td>0.016359</td>
      <td>-0.016774</td>
      <td>0.045229</td>
      <td>0.014314</td>
      <td>0.013465</td>
      <td>0.061905</td>
      <td>-0.004469</td>
      <td>...</td>
      <td>0.012852</td>
      <td>0.034246</td>
      <td>0.054216</td>
      <td>-3.728633e-03</td>
      <td>0.069408</td>
      <td>-0.038463</td>
      <td>0.000283</td>
      <td>-1.115864e-29</td>
      <td>0.011725</td>
      <td>0.005210</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.032665</td>
      <td>0.000000</td>
      <td>0.023592</td>
      <td>-0.016699</td>
      <td>-0.032420</td>
      <td>-0.019154</td>
      <td>0.062835</td>
      <td>-0.002045</td>
      <td>0.060978</td>
      <td>-0.004654</td>
      <td>...</td>
      <td>-0.002849</td>
      <td>0.012514</td>
      <td>0.080611</td>
      <td>-6.569508e-03</td>
      <td>0.076127</td>
      <td>0.088853</td>
      <td>0.054506</td>
      <td>-1.309591e-02</td>
      <td>0.032720</td>
      <td>-0.006562</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-0.032267</td>
      <td>0.023592</td>
      <td>0.000000</td>
      <td>0.042521</td>
      <td>-0.031153</td>
      <td>-0.010965</td>
      <td>0.057895</td>
      <td>-0.040328</td>
      <td>-0.021620</td>
      <td>0.003036</td>
      <td>...</td>
      <td>-0.016524</td>
      <td>0.005764</td>
      <td>-0.027753</td>
      <td>3.398820e-30</td>
      <td>0.009517</td>
      <td>0.028658</td>
      <td>0.001249</td>
      <td>4.640786e-02</td>
      <td>0.048975</td>
      <td>-0.041902</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.016359</td>
      <td>-0.016699</td>
      <td>0.042521</td>
      <td>0.000000</td>
      <td>-0.002730</td>
      <td>0.032028</td>
      <td>-0.031510</td>
      <td>0.031002</td>
      <td>0.021538</td>
      <td>-0.038158</td>
      <td>...</td>
      <td>-0.038547</td>
      <td>0.002558</td>
      <td>-0.004579</td>
      <td>-1.342204e-29</td>
      <td>-0.051202</td>
      <td>0.043721</td>
      <td>0.014981</td>
      <td>-7.301069e-02</td>
      <td>-0.011580</td>
      <td>0.035714</td>
    </tr>
    <tr>
      <th>5</th>
      <td>-0.016774</td>
      <td>-0.032420</td>
      <td>-0.031153</td>
      <td>-0.002730</td>
      <td>0.000000</td>
      <td>-0.045909</td>
      <td>0.009393</td>
      <td>0.045783</td>
      <td>0.015280</td>
      <td>-0.004929</td>
      <td>...</td>
      <td>0.019115</td>
      <td>0.013596</td>
      <td>0.000476</td>
      <td>1.127001e-02</td>
      <td>0.061089</td>
      <td>0.049306</td>
      <td>-0.023689</td>
      <td>-3.528555e-02</td>
      <td>0.017825</td>
      <td>0.064367</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 6040 columns</p>
</div>




```python
# 이제 유저간의 유사도를 계산할거임 ... ㅠㅠ 

cosine = cosine_similarity(final_movie)
np.fill_diagonal(cosine, 0)
similarity_with_movie = pd.DataFrame(cosine, index=final_movie.index)
similarity_with_movie.columns = final_user.index
similarity_with_movie.head()
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
      <td>0.000000</td>
      <td>0.953845</td>
      <td>0.972236</td>
      <td>0.980503</td>
      <td>0.917310</td>
      <td>0.971808</td>
      <td>0.982894</td>
      <td>0.957942</td>
      <td>0.971476</td>
      <td>0.892693</td>
      <td>...</td>
      <td>0.951468</td>
      <td>0.959513</td>
      <td>0.974206</td>
      <td>0.984295</td>
      <td>0.860156</td>
      <td>0.844517</td>
      <td>0.937173</td>
      <td>0.980006</td>
      <td>0.967969</td>
      <td>0.891287</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.953845</td>
      <td>0.000000</td>
      <td>0.949645</td>
      <td>0.955644</td>
      <td>0.890131</td>
      <td>0.946769</td>
      <td>0.958843</td>
      <td>0.931543</td>
      <td>0.945966</td>
      <td>0.867840</td>
      <td>...</td>
      <td>0.926948</td>
      <td>0.934609</td>
      <td>0.951314</td>
      <td>0.960502</td>
      <td>0.842766</td>
      <td>0.835665</td>
      <td>0.918411</td>
      <td>0.955374</td>
      <td>0.945531</td>
      <td>0.866613</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.972236</td>
      <td>0.949645</td>
      <td>0.000000</td>
      <td>0.977010</td>
      <td>0.910536</td>
      <td>0.967095</td>
      <td>0.979625</td>
      <td>0.951841</td>
      <td>0.964196</td>
      <td>0.888669</td>
      <td>...</td>
      <td>0.946086</td>
      <td>0.952573</td>
      <td>0.967395</td>
      <td>0.979558</td>
      <td>0.854523</td>
      <td>0.847168</td>
      <td>0.934507</td>
      <td>0.975655</td>
      <td>0.964512</td>
      <td>0.884753</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.980503</td>
      <td>0.955644</td>
      <td>0.977010</td>
      <td>0.000000</td>
      <td>0.920439</td>
      <td>0.974893</td>
      <td>0.986598</td>
      <td>0.962118</td>
      <td>0.972684</td>
      <td>0.894987</td>
      <td>...</td>
      <td>0.952766</td>
      <td>0.961831</td>
      <td>0.977141</td>
      <td>0.987630</td>
      <td>0.858413</td>
      <td>0.852880</td>
      <td>0.940970</td>
      <td>0.982864</td>
      <td>0.969556</td>
      <td>0.897799</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.917310</td>
      <td>0.890131</td>
      <td>0.910536</td>
      <td>0.920439</td>
      <td>0.000000</td>
      <td>0.909701</td>
      <td>0.924509</td>
      <td>0.902492</td>
      <td>0.907346</td>
      <td>0.836649</td>
      <td>...</td>
      <td>0.895556</td>
      <td>0.899463</td>
      <td>0.914695</td>
      <td>0.923953</td>
      <td>0.815476</td>
      <td>0.800895</td>
      <td>0.875181</td>
      <td>0.919466</td>
      <td>0.908107</td>
      <td>0.840375</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 6040 columns</p>
</div>




```python
# 이제 탑 1~30까지 구해보자 

def find_n_neighbours(df,n):
    order = np.argsort(df.values, axis=1)[:, :n]
    df = df.apply(lambda x: pd.Series(x.sort_values(ascending=False)
           .iloc[:n].index, 
          index=['top{}'.format(i) for i in range(1, n+1)]), axis=1)
    return df

# find_n_neighbours 함수 선언
```


```python
sim_user_30_u = find_n_neighbours(similarity_with_user, 30)
sim_user_30_u.head()
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
      <th>top1</th>
      <th>top2</th>
      <th>top3</th>
      <th>top4</th>
      <th>top5</th>
      <th>top6</th>
      <th>top7</th>
      <th>top8</th>
      <th>top9</th>
      <th>top10</th>
      <th>...</th>
      <th>top21</th>
      <th>top22</th>
      <th>top23</th>
      <th>top24</th>
      <th>top25</th>
      <th>top26</th>
      <th>top27</th>
      <th>top28</th>
      <th>top29</th>
      <th>top30</th>
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
      <td>1337</td>
      <td>379</td>
      <td>5404</td>
      <td>49</td>
      <td>2607</td>
      <td>5739</td>
      <td>5635</td>
      <td>2495</td>
      <td>4159</td>
      <td>4724</td>
      <td>...</td>
      <td>2345</td>
      <td>6008</td>
      <td>942</td>
      <td>2766</td>
      <td>1568</td>
      <td>89</td>
      <td>1283</td>
      <td>933</td>
      <td>2224</td>
      <td>1311</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1546</td>
      <td>4248</td>
      <td>4975</td>
      <td>4320</td>
      <td>82</td>
      <td>2771</td>
      <td>5864</td>
      <td>5353</td>
      <td>2765</td>
      <td>3540</td>
      <td>...</td>
      <td>2393</td>
      <td>5175</td>
      <td>1739</td>
      <td>3295</td>
      <td>2814</td>
      <td>4313</td>
      <td>4148</td>
      <td>2485</td>
      <td>4505</td>
      <td>5689</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5709</td>
      <td>5417</td>
      <td>84</td>
      <td>5635</td>
      <td>1510</td>
      <td>5497</td>
      <td>3753</td>
      <td>686</td>
      <td>5478</td>
      <td>3148</td>
      <td>...</td>
      <td>2490</td>
      <td>2463</td>
      <td>5732</td>
      <td>410</td>
      <td>4320</td>
      <td>5879</td>
      <td>4603</td>
      <td>4915</td>
      <td>4129</td>
      <td>455</td>
    </tr>
    <tr>
      <th>4</th>
      <td>446</td>
      <td>491</td>
      <td>1236</td>
      <td>3186</td>
      <td>5119</td>
      <td>3263</td>
      <td>4030</td>
      <td>2227</td>
      <td>5819</td>
      <td>51</td>
      <td>...</td>
      <td>2354</td>
      <td>205</td>
      <td>3535</td>
      <td>3658</td>
      <td>5332</td>
      <td>4632</td>
      <td>481</td>
      <td>3580</td>
      <td>4947</td>
      <td>3915</td>
    </tr>
    <tr>
      <th>5</th>
      <td>3899</td>
      <td>5694</td>
      <td>3267</td>
      <td>1211</td>
      <td>4860</td>
      <td>1636</td>
      <td>5826</td>
      <td>5440</td>
      <td>5749</td>
      <td>1484</td>
      <td>...</td>
      <td>1087</td>
      <td>5797</td>
      <td>498</td>
      <td>5378</td>
      <td>1519</td>
      <td>4620</td>
      <td>2947</td>
      <td>3685</td>
      <td>39</td>
      <td>752</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 30 columns</p>
</div>




```python
sim_user_30_m = find_n_neighbours(similarity_with_movie,30)
sim_user_30_m.head()
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
      <th>top1</th>
      <th>top2</th>
      <th>top3</th>
      <th>top4</th>
      <th>top5</th>
      <th>top6</th>
      <th>top7</th>
      <th>top8</th>
      <th>top9</th>
      <th>top10</th>
      <th>...</th>
      <th>top21</th>
      <th>top22</th>
      <th>top23</th>
      <th>top24</th>
      <th>top25</th>
      <th>top26</th>
      <th>top27</th>
      <th>top28</th>
      <th>top29</th>
      <th>top30</th>
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
      <td>3324</td>
      <td>4628</td>
      <td>592</td>
      <td>5007</td>
      <td>283</td>
      <td>5168</td>
      <td>4073</td>
      <td>1454</td>
      <td>1986</td>
      <td>2184</td>
      <td>...</td>
      <td>907</td>
      <td>5694</td>
      <td>4741</td>
      <td>3730</td>
      <td>4010</td>
      <td>1568</td>
      <td>277</td>
      <td>2339</td>
      <td>1307</td>
      <td>4926</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2467</td>
      <td>2111</td>
      <td>1454</td>
      <td>592</td>
      <td>367</td>
      <td>2268</td>
      <td>4628</td>
      <td>124</td>
      <td>4073</td>
      <td>2388</td>
      <td>...</td>
      <td>5007</td>
      <td>1669</td>
      <td>1801</td>
      <td>1986</td>
      <td>5168</td>
      <td>20</td>
      <td>128</td>
      <td>4741</td>
      <td>1708</td>
      <td>2339</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3743</td>
      <td>2111</td>
      <td>5122</td>
      <td>4010</td>
      <td>1986</td>
      <td>2268</td>
      <td>3287</td>
      <td>5168</td>
      <td>213</td>
      <td>2574</td>
      <td>...</td>
      <td>4881</td>
      <td>3421</td>
      <td>5068</td>
      <td>4741</td>
      <td>4537</td>
      <td>4038</td>
      <td>2538</td>
      <td>4254</td>
      <td>4665</td>
      <td>298</td>
    </tr>
    <tr>
      <th>4</th>
      <td>446</td>
      <td>5168</td>
      <td>1236</td>
      <td>3828</td>
      <td>4073</td>
      <td>2295</td>
      <td>4176</td>
      <td>907</td>
      <td>4010</td>
      <td>2729</td>
      <td>...</td>
      <td>4100</td>
      <td>5781</td>
      <td>2268</td>
      <td>4288</td>
      <td>5696</td>
      <td>1245</td>
      <td>455</td>
      <td>5007</td>
      <td>2184</td>
      <td>298</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5694</td>
      <td>3899</td>
      <td>1844</td>
      <td>5309</td>
      <td>782</td>
      <td>4664</td>
      <td>4628</td>
      <td>5440</td>
      <td>2633</td>
      <td>277</td>
      <td>...</td>
      <td>1815</td>
      <td>5007</td>
      <td>298</td>
      <td>1811</td>
      <td>4558</td>
      <td>276</td>
      <td>681</td>
      <td>5904</td>
      <td>427</td>
      <td>171</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 30 columns</p>
</div>




```python
# 두 유저를 입력받고 
def get_user_similar_movies( user1, user2 ):
    common_movies = Rating_avg[Rating_avg.user_id == user1].merge(
    Rating_avg[Rating_avg.user_id == user2],
    on = "movie_id",
    how = "inner" )
    return common_movies.merge( movies, on = 'movie_id' )
```


```python
a = get_user_similar_movies(2,5)
a = a.loc[ : , ['rating_x_x','rating_x_y','movie']]
a.head()
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
      <th>rating_x_x</th>
      <th>rating_x_y</th>
      <th>movie</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5</td>
      <td>2</td>
      <td>Few Good Men, A (1992)</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>1</td>
      <td>Total Recall (1990)</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>5</td>
      <td>GoodFellas (1990)</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5</td>
      <td>2</td>
      <td>Gladiator (2000)</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>2</td>
      <td>Awakenings (1990)</td>
    </tr>
  </tbody>
</table>
</div>




```python
def User_item_score(user,item):
    a = sim_user_30_m[sim_user_30_m.index==user].values
    b = a.squeeze().tolist()
    c = final_movie.loc[:,item]
    d = c[c.index.isin(b)]
    f = d[d.notnull()]
    avg_user = Mean.loc[Mean['user_id'] == user,'rating'].values[0]
    index = f.index.values.squeeze().tolist()
    corr = similarity_with_movie.loc[user,index]
    fin = pd.concat([f, corr], axis=1)
    fin.columns = ['adg_score','correlation']
    fin['score']=fin.apply(lambda x:x['adg_score'] * x['correlation'],axis=1)
    nume = fin['score'].sum()
    deno = fin['correlation'].sum()
    final_score = avg_user + (nume/deno)
    return final_score
```


```python
score = User_item_score(2,5)
print("score (u,i) is",score)
#어느정도 유사도인지 알려주는거
```

    score (u,i) is 3.293401738351707
    


```python
Rating_avg = Rating_avg.astype({"movie_id": str})
Movie_user = Rating_avg.groupby(by = 'user_id')['movie_id'].apply(lambda x:','.join(x))
```


```python
def User_item_score1(user):
    Movie_seen_by_user = check.columns[check[check.index==user].notna().any()].tolist()
    a = sim_user_30_m[sim_user_30_m.index==user].values
    b = a.squeeze().tolist()
    d = Movie_user[Movie_user.index.isin(b)]
    l = ','.join(d.values)
    Movie_seen_by_similar_users = l.split(',')
    Movies_under_consideration = list(set(Movie_seen_by_similar_users)-set(list(map(str, Movie_seen_by_user))))
    Movies_under_consideration = list(map(int, Movies_under_consideration))
    score = []
    for item in Movies_under_consideration:
        c = final_movie.loc[:,item]
        d = c[c.index.isin(b)]
        f = d[d.notnull()]
        avg_user = Mean.loc[Mean['user_id'] == user,'rating'].values[0]
        index = f.index.values.squeeze().tolist()
        corr = similarity_with_movie.loc[user,index]
        fin = pd.concat([f, corr], axis=1)
        fin.columns = ['adg_score','correlation']
        fin['score']=fin.apply(lambda x:x['adg_score'] * x['correlation'],axis=1)
        nume = fin['score'].sum()
        deno = fin['correlation'].sum()
        final_score = avg_user + (nume/deno)
        score.append(final_score)
    data = pd.DataFrame({'movie_id':Movies_under_consideration,'score':score})
    top_5_recommendation = data.sort_values(by='score',ascending=False).head(5)
    Movie_Name = top_5_recommendation.merge(movies, how='inner', on='movie_id')
    Movie_Names = Movie_Name.movie.values.tolist()
    return Movie_Names
```


```python
user = int(input("유저 아이디 입력 : "))
predicted_movies = User_item_score1(user)
print(" ")
print("유저 아이디 : 370")
print("   ")
print("-------------------------------------추천영화----------------")
for i in predicted_movies:
    print(i)
print("-------------------------------------------------------------")
print("됐다 ㅎㅎ 다음은 item_based 세계로 .. ")
```

    유저 아이디 입력 : 1994
     
    유저 아이디 : 370
       
    -------------------------------------추천영화----------------
    Close Shave, A (1995)
    Shawshank Redemption, The (1994)
    Wrong Trousers, The (1993)
    Sixth Sense, The (1999)
    Raiders of the Lost Ark (1981)
    -------------------------------------------------------------
    됐다 ㅎㅎ 다음은 item_based 세계로 .. 
    


```python

```
