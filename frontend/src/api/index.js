import axios from "axios";

//const apiUrl = "http://127.0.0.1:8000/api";
const apiUrl = "http://52.79.111.26:8000/api";

export default {
    searchMovies(params) {
        return axios.get(`${apiUrl}/movies/`, {
            params
        });
    },
    searchRatings(params) {
        return axios.get(`${apiUrl}/ratings/`, {
            params
        });
    },
    serachProfiles(params) {
        return axios.get(`${apiUrl}/profiles/`, {
            params
        });
    },
    updateMovie(data) {
        const genre = data.genres.replace("/,/gi", "|");

        const movie = {
            id: data.id,
            title: data.title,
            genres: genre
        };
    return axios.put(`${apiUrl}/movies/`, movie);
    },
    updateProfile(data) {
      return axios.put(`${apiUrl}/profiles/`, data);
    },
    updateRating(data) {
      return axios.put(`${apiUrl}/ratings/`, data);
    },
    classifyingMovies(params) {
      return axios.get(`${apiUrl}/classify/`, { params });
    },
    userbased_recommendMovies(params) {
      return axios.get(`${apiUrl}/userbased`, {params});
    },
    itembased_recommendMovies(params) {
      return axios.get(`${apiUrl}/itembased`, {params});
    },
    matrix_recommendMovies(params) {
      return axios.get(`${apiUrl}/matrixfactorization`, {params});
    },
    movie_image(params){
      return axios.get(`${apiUrl}/imageurl`, {params});
    }
};
