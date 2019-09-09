<!-- 분류 검색 페이지 -->
<template>
  <v-container grid-list-md text-center>
    <v-layout justify-center wrap>
      <!-- 검색 폼 -->
      <v-flex xs6>
        <div class="display-2 pa-10">분류 검색</div>
        <ClassifySearchForm :submit="classifySearch" />
      </v-flex>
      <!-- 검색 결과 -->
      <v-flex xs7>
        <ClassifyList :classify-list-cards="classifyList" />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";
import ClassifySearchForm from "../ClassifySearchForm";
import ClassifyList from "../ClassifyList";
export default {
  components: {
    ClassifyList,
    ClassifySearchForm
  },
  data: () => ({}),
  computed: {
    ...mapState({
      classifyList: state => state.data.classifiedList
    })
  },
  methods: mapActions("data", ["classifySearch"])
};
</script>
