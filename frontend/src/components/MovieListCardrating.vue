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
                        v-model="rating"
                        color="indigo"
                        background-color="indigo"
                        dense
                        half-increments
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
              <br />내용이 들어갈 곳입니다.
            </v-card-text>
            <v-btn @click="addrate" color="grey" align-center>Check</v-btn>
          </v-card>
        </v-dialog>
      </v-layout>
    </v-card>
  </v-hover>
</template>

<script>
import axios from 'axios'
//import api from '../../api/'

const apiUrl ="/api"
import { mapActions } from "vuex";
export default {
  components: {
    axios
  },
  
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
    },
    
  },
  data() {
    return {
      rating: 2, 
      dialog: false
      
    };
  },
  computed: {
    genresStr: function() {
      return this.genres.join(" / ");
    }
  },
  methods:{
    
    addrate: function(){
      let params={

      }
    }
  }
};
</script>