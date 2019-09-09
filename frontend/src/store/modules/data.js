import api from "../../api";

// initial state
const state = {
  // shape: [{ id, title, genres, viewCnt, rating }]
  movieSearchList: [],
  // For Admin Data
  AllMovieList: [],
  AllProfileList: [],
  AllRatingList: [],
  classifiedList: []
};

// actions
const actions = {
  async searchMovies({ commit }, params) {
    const resp = await api.searchMovies(params);
    const movies = resp.data.map(d => ({
      id: d.id,
      title: d.title,
      genres: d.genres_array,
      viewCnt: d.view_cnt,
      rating: d.average_rating,
      occupation_array: d.occupation_array
    }));

    commit("setMovieSearchList", movies);
  },
  async searchProfiles({ commit }, params) {
    const resp = await api.serachProfiles(params);
    const profiles = resp.data.map(d => ({
      id: d.id,
      username: d.username,
      is_staff: d.is_staff,
      gender: d.gender,
      age: d.age,
      occupation: d.occupation
    }));

    commit("setProfileSearchList", profiles);
  },
  async searchRatings({ commit }, params) {
    const resp = await api.searchRatings(params);
    const ratings = resp.data.map(d => ({
      id: d.id,
      userid: d.userid,
      movieid: d.movieid,
      rating: d.rating,
      timestamp: d.timestamp
    }));

    commit("setRatingSearchList", ratings);
  },
  async getAllMovies({ commit }, params) {
    const resp = await api.searchMovies(params);
    const movies = resp.data.map(d => ({
      id: d.id,
      title: d.title,
      genres: d.genres_array,
      viewCnt: d.view_cnt,
      rating: d.average_rating,
      occupation_array: d.occupation_array
    }));

    commit("setAllMoviesData", movies);
  },
  async getAllProfiles({ commit }, params) {
    const resp = await api.serachProfiles(params);
    const profiles = resp.data.map(d => ({
      id: d.id,
      username: d.username,
      is_staff: d.is_staff,
      gender: d.gender,
      age: d.age,
      occupation: d.occupation
    }));

    commit("setAllProfilesData", profiles);
  },
  async getAllRatings({ commit }, params) {
    const resp = await api.searchRatings(params);
    const ratings = resp.data.map(d => ({
      id: d.id,
      userid: d.userid,
      movieid: d.movieid,
      rating: d.rating,
      timestamp: d.timestamp
    }));

    commit("setAllRatingsData", ratings);
  },
  async classifySearch({ commit }, params) {
    const resp = await api.classifyingMovies(params);
    const movies = resp.data.map(d => ({
      id: d.id,
      title: d.title,
      genres: d.genres_array,
      viewCnt: d.view_cnt,
      rating: d.average_rating,
      occupation_array: d.occupation_array
    }));
    console.log(movies.length);

    console.log("121212");

    commit("setClassifiedMovies", movies);
  }
};

// mutations
const mutations = {
  setMovieSearchList(state, movies) {
    state.movieSearchList = movies.map(m => m);
  },
  setMovieSorted(state, division) {
    const movieData = state.movieSearchList;
    movieData.sort((a, b) => {
      let compare = 0;
      if (division == "rating") {
        if (a.rating > b.rating) {
          compare = -1;
        } else if (b.rating > a.rating) {
          compare = 1;
        }
        return compare;
      } else if (division == "viewCnt") {
        if (a.viewCnt > b.viewCnt) {
          compare = -1;
        } else if (b.viewCnt > a.viewCnt) {
          compare = 1;
        }
        return compare;
      } else if (division == "id") {
        if (a.id > b.id) {
          compare = 1;
        } else if (b.id > a.id) {
          compare = -1;
        }
        return compare;
      }
    });
    state.movieSearchList = movieData;
  },
  setMovieSearchList_occupation(state, select_occupation) {
    const movieData = state.movieSearchList;
    movieData.sort((a, b) => {
      let compare = 0;
      if (
        a.occupation_array[select_occupation] >
        b.occupation_array[select_occupation]
      ) {
        compare = -1;
      } else if (
        b.occupation_array[select_occupation] >
        a.occupation_array[select_occupation]
      ) {
        compare = 1;
      }
      return compare;
    });

    state.movieSearchList = movieData;
  },
  setAllProfilesData(state, profiles) {
    state.AllProfileList = profiles.map(m => m);
  },
  setAllMoviesData(state, movies) {
    state.AllMovieList = movies.map(m => m);
  },
  setAllRatingsData(state, ratings) {
    state.AllRatingList = ratings.map(m => m);
  },
  setClassifiedMovies(state, movies) {
    state.classifiedList = movies.map(m => m);
    console.log(state.classifiedList.length);
    console.log("setter");
  }
};

//default
export default {
  namespaced: true,
  state,
  actions,
  mutations
};
