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
              <v-flex v-for="movie in recommendList" :key="movie.id">
                <v-card max-width="344" class="mx-auto">
                  <v-card-title class="headline">{{ movie }}</v-card-title>
                </v-card>
              </v-flex>
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

const apiUrl = "/api";

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
      recommendList: []
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
      const result = await axios.get(`http://localhost:8000/api/likemovie`, this.id);
      this.recommendList = result.recommend_list_title;
    }
  }
};
</script>