import axios from "axios";

const apiUrl = "/api";

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
  signup(params){
        console.log(params)
        return axios.post(`${apiUrl}/auth/signup-many/`,params);
  }
};
