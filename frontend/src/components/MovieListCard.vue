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
              <v-layout>
              <v-flex xs5>
              장르 : {{ genresStr }}
              <br />
              평점 : {{ rating.toFixed(1) }}
              <br />
              시청수 : {{ viewCnt }}
              <br />
              <br />
              <br />
              <br />
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
                  <v-sheet class="text-center" height="470px" color=rgba(0,0,0,0.7)>
                    <v-layout>
                      <v-flex sm1/>
                      <v-flex sm2 v-for="movie1 in user_recommendList" :key="movie1.id">
                        <div style="padding:20px;">
                          <p style="color: white; font-size:20px;">{{movie1}}</p>
                        </div>
                      </v-flex>
                      <v-flex sm1/>
                    </v-layout><v-layout>
                      <v-flex sm1/>
                      <v-flex sm2 v-for="movie1_url in user_recommendList_url" :key="movie1_url.url">
                        <div style="padding:20px;">
                          <v-img
                            :src = movie1_url
                            aspect-ratio="1"
                            class="grey lighten-2"
                            max-width="300"
                            max-height="500"
                          ></v-img>
                        </div>
                      </v-flex>
                      <v-flex sm1/>
                    </v-layout>
                  
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
                  <v-sheet class="text-center" height="470px" color=rgba(0,0,0,0.7)>
                    <v-layout>
                      <v-flex sm1/>
                      <v-flex sm2 v-for="movie2 in item_recommendList" :key="movie2.id">
                        <div style="padding:20px;">
                          <p style="color: white; font-size:20px;">{{movie2}}</p>
                        </div>
                      </v-flex>
                      <v-flex sm1/>
                    </v-layout><v-layout>
                      <v-flex sm1/>
                      <v-flex sm2 v-for="movie2_url in item_recommendList_url" :key="movie2_url.url">
                        <div style="padding:20px;">
                          <v-img
                            :src = movie2_url
                            aspect-ratio="1"
                            class="grey lighten-2"
                            max-width="300"
                            max-height="500"
                          ></v-img>
                        </div>
                      </v-flex>
                      <v-flex sm1/>
                    </v-layout>
                  
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
                  <v-sheet class="text-center" height="470px" color=rgba(0,0,0,0.7)>
                    <v-layout>
                      <v-flex sm1/>
                      <v-flex sm2 v-for="movie3 in matrix_recommendList" :key="movie3.id">
                        <div style="padding:20px;">
                          <p style="color: white; font-size:20px;">{{movie3}}</p>
                        </div>
                      </v-flex>
                      <v-flex sm1/>
                    </v-layout><v-layout>
                      <v-flex sm1/>
                      <v-flex sm2 v-for="movie3_url in matrix_recommendList_url" :key="movie3_url.url">
                        <div style="padding:20px;">
                          <v-img
                            :src = movie3_url
                            aspect-ratio="1"
                            class="grey lighten-2"
                            max-width="300"
                            max-height="500"
                          ></v-img>
                        </div>
                      </v-flex>
                      <v-flex sm1/>
                    </v-layout>
                  
                  </v-sheet>
                </v-bottom-sheet>
              </div>
              </v-flex>

              <v-flex xs7>
              <v-img
                :src = imgurl
                aspect-ratio="1"
                class="grey lighten-2"
                max-width="300"
                max-height="500"
              ></v-img>
              </v-flex>
              </v-layout>
              <br />
              

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
      user_recommendList_url: [],
      item_recommendList_url: [],
      matrix_recommendList_url: [],
      sheet_user: false,
      sheet_item: false,
      sheet_matrix: false,
      imgurl:"https://i.imgur.com/tq6diZs.jpg"
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
      const params = {movieid: this.id};
      const imgurl_result = await api.movie_image(params);
      const user_result = await api.userbased_recommendMovies(params);
      const item_result = await api.itembased_recommendMovies(params);
      const matrix_result = await api.matrix_recommendMovies(params);
      console.log(matrix_result)
      this.user_recommendList = user_result.data[0].recommend_list_title;
      this.item_recommendList = item_result.data[0].recommend_list_title;
      this.matrix_recommendList = matrix_result.data[0].recommend_list_title;
      this.user_recommendList_url = user_result.data[0].recommend_list_url;
      this.item_recommendList_url = item_result.data[0].recommend_list_url;
      this.matrix_recommendList_url = matrix_result.data[0].recommend_list_url;
      
      // 여기서 예외 처리 해주기 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  
      this.imgurl = imgurl_result.data[0].url;
    }
  }
};
</script>