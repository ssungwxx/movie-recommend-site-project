<template>
    <v-container grid-list-md text-center>
        <v-layout justify-left wrap>
            <v-flex xs5>
                <v-select v-model="param" :items="dataDivision" label="데이터 선택"></v-select>
            </v-flex>
            <v-flex xs12>
                <AdminMovieDataList :movieData="movieList" v-if="param==='영화'" />
                <AdminProfileDataList :profileData="profileList" v-if="param==='사용자'" />
                <AdminRatingDataList :ratingData="ratingList" v-if="param==='평점'" />
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";
import AdminMovieDataList from "../AdminMovieDataList";
import AdminProfileDataList from "../AdminProfileDataList";
import AdminRatingDataList from "../AdminRatingDataList";

export default {
    components: {
        AdminMovieDataList,
        AdminProfileDataList,
        AdminRatingDataList
    },
    data: () => ({
        param: "",
        dataDivision: ["사용자", "영화", "평점"],
        movieSearchList: [],
        profileSearchList: [],
        ratingSearchList: []
    }),
    methods: {},
    computed: {
        ...mapState({
            movieList: state => state.data.AllMovieList
        }),
        ...mapState({
            profileList: state => state.data.AllProfileList
        }),
        ...mapState({
            ratingList: state => state.data.AllRatingList
        })
    },
    watch: {
        param: async function() {
            if (this.profileSearchList.length == 0 && this.param == "사용자") {
                await this.$store.dispatch("data/getAllProfiles");
            } else if (
                this.movieSearchList.length == 0 &&
                this.param == "영화"
            ) {
                await this.$store.dispatch("data/getAllMovies");
            } else if (
                this.ratingSearchList.length == 0 &&
                this.param == "평점"
            ) {
                await this.$store.dispatch("data/getAllRatings");
            }
        }
    }
};
</script>