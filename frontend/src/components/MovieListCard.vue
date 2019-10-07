<template>
  <v-hover v-slot:default="{ hover }">
    <v-card :elevation="hover ? 8 : 2">
      <v-layout align-center py-4 pl-4>
        <v-dialog v-model="dialog" width="600px">
          <template v-slot:activator="{ on }">
            <v-flex text-center v-on="on">
              <v-container grid-list-lg pa-0>
                <v-layout column>
                  <v-list-item>
                    <v-list-item-content>
                      <v-list-item-title class="headline">{{ title }}</v-list-item-title>
                      <v-list-item-subtitle>{{ genresStr }}</v-list-item-subtitle>
                    </v-list-item-content>
                  </v-list-item>
                  <v-card-text>
                    <v-layout justify-center>
                      <v-rating
                        :value="rating"
                        color="indigo"
                        background-color="indigo"
                        half-increments
                        dense
                        readonly
                      />
                      <div class="grey--text ml-4">{{ rating.toFixed(1) }}</div>
                    </v-layout>
                  </v-card-text>
                  <v-card-text>
                    <v-layout justify-center>
                      <v-icon color="black">mdi-eye</v-icon>
                      <div class="grey--text ml-4">{{ viewCnt }}</div>
                    </v-layout>
                  </v-card-text>
                </v-layout>
              </v-container>
            </v-flex>
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">{{ title }}</span>
            </v-card-title>
            <v-card-text>
              장르 : {{ genresStr }}
              <br />
              평점 : {{ rating.toFixed(1) }}
              <br />
              시청수 : {{ viewCnt }}
              <br />
              <br />
              <div class="text-center">
                <v-bottom-sheet v-model="sheet_user">
                  <template v-slot:activator="{ on }">
                    <v-btn text large
                      v-on="on"
                    >
                      User_based
                    </v-btn>
                  </template>
                    <v-sheet class="text-center" height="300px">
                      <v-flex v-for="movie1 in user_recommendList" :key="movie1.id">
                        <v-card max-width="1000" class="mx-auto">
                        <v-card-title class="headline">{{ movie1 }}</v-card-title>
                      </v-card>
                    </v-flex>
                  </v-sheet>
                </v-bottom-sheet>
              </div>
              <div class="text-center">
                <v-bottom-sheet v-model="sheet_item">
                  <template v-slot:activator="{ on }">
                    <v-btn text large
                      color="error"
                      v-on="on"
                    >
                      Item_based
                    </v-btn>
                  </template>
                  <v-sheet class="text-center" height="300px">
                      <v-flex v-for="movie2 in item_recommendList" :key="movie2.id">
                        <v-card max-width="1000" class="mx-auto">
                        <v-card-title class="headline">{{ movie2 }}</v-card-title>
                      </v-card>
                    </v-flex>
                  </v-sheet>
                </v-bottom-sheet>
              </div>
              <div class="text-center">
                <v-bottom-sheet v-model="sheet_matrix">
                  <template v-slot:activator="{ on }">
                    <v-btn text large
                      color="primary"
                      v-on="on"
                    >
                      Matrix_Factorization
                    </v-btn>
                  </template>
                  <v-sheet class="text-center" height="300px">
                      <v-flex v-for="movie3 in matrix_recommendList" :key="movie3.id">
                        <v-card max-width="1000" class="mx-auto">
                        <v-card-title class="headline">{{ movie3 }}</v-card-title>
                      </v-card>
                    </v-flex>
                  </v-sheet>
                </v-bottom-sheet>
              </div>

              <!-- <v-flex v-for="movie in recommendList" :key="movie.id">
                <v-card max-width="344" class="mx-auto">
                  <v-card-title class="headline">{{ movie }}</v-card-title>
                </v-card>
              </v-flex> -->
            </v-card-text>
          </v-card>
        </v-dialog>
      </v-layout>
    </v-card>
  </v-hover>
</template>

<script>
import { mapActions } from "vuex";
import axios from "axios";

import api from "../api";

export default {
  props: {
    id: {
      type: Number,
      default: 0
    },
    title: {
      type: String,
      default: ""
    },
    genres: {
      type: Array,
      default: () => new Array()
    },
    img: {
      type: String,
      default: ""
    },
    rating: {
      type: Number,
      default: 0.0
    },
    viewCnt: {
      type: Number,
      default: 0
    }
  },
  data() {
    return {
      dialog: false,
      user_recommendList: [],
      item_recommendList: [],
      matrix_recommendList: [],
      sheet_user: false,
      sheet_item: false,
      sheet_matrix: false
    };
  },
  mounted() {
    this.recommend();
  },
  computed: {
    genresStr: function() {
      return this.genres.join(" / ");
    }
  },
  methods: {
    async recommend() {
      const params = {movieid: this.id}
      const user_result = await api.userbased_recommendMovies(params);
      const item_result = await api.itembased_recommendMovies(params);
      const matrix_result = await api.matrix_recommendMovies(params);
      this.user_recommendList = user_result.data[0].recommend_list_title;
      this.item_recommendList = item_result.data[0].recommend_list_title;
      this.matrix_recommendList = matrix_result.data[0].recommend_list_title;
    }
  }
};
</script>