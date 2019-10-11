<template>
  <v-form ref="form">
    <v-text-field xs6 v-model="param" label="검색어" />
    <v-layout justify-center pa-10>
      <v-btn large color="indigo white--text" @click="onSubmit">Search</v-btn>
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
    param: ""
  }),
  methods: {
    onSubmit: function() {
      let params = "";
        params = {
          title: this.param
        };
         
      if (!params == "") this.submit(params);
    }
  }
};
</script>