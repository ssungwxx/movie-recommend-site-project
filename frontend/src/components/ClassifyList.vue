<template>
  <v-container class="pa-2" fluid grid-list-md>
    <v-layout column>
      <v-flex v-for="card in classifyListCardsSliced" :key="card.id" pa-2>
        <ClassifyListCard
          :id="card.id"
          :img="card.img"
          :title="card.title"
          :genres="card.genres"
          :rating="card.rating"
          :view-cnt="card.viewCnt"
        />
      </v-flex>
      <v-pagination v-if="maxPages > 1" v-model="page" :length="maxPages" />
    </v-layout>
  </v-container>
</template>

<script>
import ClassifyListCard from "./ClassifyListCard";
export default {
  components: {
    ClassifyListCard
  },
  props: {
    classifyListCards: {
      type: Array,
      default: () => new Array()
    }
  },
  data: () => ({
    cardsPerPage: 10,
    page: 1
  }),
  computed: {
    // pagination related variables
    classifyListEmpty: function() {
      return this.classifyListCards.length === 0;
    },
    maxPages: function() {
      return Math.floor(
        (this.classifyListCards.length + this.cardsPerPage - 1) /
          this.cardsPerPage
      );
    },
    classifyListCardsSliced: function() {
      return this.classifyListCards.slice(
        this.cardsPerPage * (this.page - 1),
        this.cardsPerPage * this.page
      );
    }
  }
};
</script>