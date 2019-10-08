import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import pairwise_distances


def find_n_neighbours(df,n):
    order = np.argsort(df.values, axis=1)[:, :n]
    df = df.apply(lambda x: pd.Series(x.sort_values(ascending=False)
           .iloc[:n].index,
          index=['top{}'.format(i) for i in range(1, n+1)]), axis=1)
    return df


def get_user_similar_movies( user1, user2 ):
    common_movies = Rating_avg[Rating_avg.user_id == user1].merge(
    Rating_avg[Rating_avg.user_id == user2],
    on = "movie_id",
    how = "inner" )
    return common_movies.merge( movies, on = 'movie_id' )


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
    Movie_Names = Movie_Name.movie_id.values.tolist()
    return Movie_Names


def main():
    movies = pd.read_csv("movies.csv",encoding="Latin1")
    Ratings = pd.read_csv("ratings.csv")
    Users = pd.read_csv("users.csv", encoding='utf-8')

    Mean = Ratings.groupby(by="user_id",as_index=False)['rating'].mean()
    Rating_avg = pd.merge(Ratings,Mean,on='user_id')
    Rating_avg['adg_rating']=Rating_avg['rating_x']-Rating_avg['rating_y']
    check = pd.pivot_table(Rating_avg, values='rating_x', index='user_id', columns='movie_id')

    final = pd.pivot_table(Rating_avg,values='adg_rating', index='user_id', columns='movie_id')
    final_movie = final.fillna(final.mean(axis=0))
    final_user = final.apply(lambda row: row.fillna(row.mean()), axis=1)


    b = cosine_similarity(final_user)
    np.fill_diagonal(b, 0 )
    similarity_with_user = pd.DataFrame(b,index=final_user.index)
    similarity_with_user.columns=final_user.index

    cosine = cosine_similarity(final_movie)
    np.fill_diagonal(cosine, 0)
    similarity_with_movie = pd.DataFrame(cosine, index=final_movie.index)
    similarity_with_movie.columns = final_user.index


    sim_user_30_u = find_n_neighbours(similarity_with_user, 30)
    sim_user_30_m = find_n_neighbours(similarity_with_movie,30)


    Rating_avg = Rating_avg.astype({"movie_id": str})
    Movie_user = Rating_avg.groupby(by = 'user_id')['movie_id'].apply(lambda x:','.join(x))

    size = Users.index.size
    preprocessing_data = np.zeros((size,6))

    for item in Users.user_id:
        print(item)
        idx = (int(item)-1)
        preprocessing_data[idx,0] = idx
        predicted_movies_user_based = User_item_score1(idx)
        cnt = 1
        for pmub in predicted_movies_user_based:
            preprocessing_data[idx,cnt] = pmub
            cnt = cnt + 1



    preprocessing_data = preprocessing_data.astype(int)
    np.savetxt('user_based_KNN.dat', preprocessing_data, delimiter='::', fmt='%d')  # array data를 .dat 파일로 변환시켜서 저장



if __name__ == '__main__':
    main()
