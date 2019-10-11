<template>
 <v-container grid-list-md text-center>
    <v-layout justify-center wrap>
      <!-- 검색 폼 -->
      <v-flex xs6>
        <div class="display-2 pa-10">관람 영화 검색</div>
        <SeeMovieSearchForm :submit="searchMovies " />
      </v-flex>
      <!-- 검색 결과 -->
      <v-flex xs7>
        <GiveMovieList :movie-list-cards="movieList" />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";
import SeeMovieSearchForm from "../SeeMovieSearchForm";
import GiveMovieList from "../GiveMovieList";
export default {
  components: {
    GiveMovieList,
    SeeMovieSearchForm
  },
  data: () => ({}),
  computed: {
    ...mapState({
      movieList: state => state.data.movieSearchList
    })
  },
  methods: mapActions("data", ["searchMovies"])
};
</script>
