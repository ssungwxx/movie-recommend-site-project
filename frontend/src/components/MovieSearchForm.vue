<template>
  <v-form ref="form">
    <v-select v-model="searchDivision" :items="searchItems" label="검색 구분"></v-select>
    <v-select v-model="sortDivision" :items="sortItems" label="정렬 구분"></v-select>
    <v-text-field xs6 v-model="param" label="검색어" />
    <v-layout justify-center pa-10>
      <v-btn large color="#666666 white--text" @click="onSubmit">Search</v-btn>
    </v-layout>
  </v-form>
</template>

<script>
export default {
  props: {
    submit: {
      type: Function,
      default: () => {}
    }
  },
  data: () => ({
    param: "",
    searchDivision: "제목",
    searchItems: ["제목", "장르"],
    sortDivision: "ID",
    sortItems: ["ID", "평점", "조회수"]
  }),
  watch: {
    sortDivision: function() {
      if (this.sortDivision == "ID") {
        this.$store.commit("data/setMovieSorted", "id");
      } else if (this.sortDivision == "평점") {
        this.$store.commit("data/setMovieSorted", "rating");
      } else if (this.sortDivision == "조회수") {
        this.$store.commit("data/setMovieSorted", "viewCnt");
      }
    }
  },
  methods: {
    onSubmit: function() {
      let params = "";
      if (this.searchDivision == "제목") {
        params = {
          title: this.param
        };
      } else if (this.searchDivision == "장르") {
        params = {
          genre: this.param
        };
      }
      if (!params == "") this.submit(params);
    }
  }
};
</script>