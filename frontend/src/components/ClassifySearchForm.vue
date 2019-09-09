<template>
  <v-form ref="form">
    <v-btn class="genderSelect" color="primary" dark @click="clickGender">성 별</v-btn>&nbsp;&nbsp;&nbsp;&nbsp;
    <v-btn class="ageSelect" color="warning" dark @click="clickAge">연 령</v-btn>&nbsp;&nbsp;&nbsp;&nbsp;
    <v-btn class="jobSelect" color="success" dark @click="clickJob">직 업</v-btn>
    <br />
    <template v-if="select === 'gender'">
      <v-select v-model="genderDivision" :items="genderItems" label="정렬 구분"></v-select>
    </template>
    <template v-if="select === 'age'">
      <v-select v-model="ageDivision" :items="ageItems" label="정렬 구분"></v-select>
    </template>
    <template v-if="select === 'job'">
      <v-select v-model="jobDivision" :items="jobItems" label="정렬 구분"></v-select>
    </template>
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
    param: "",
    genderDivision: "남",
    genderItems: ["남", "여"],
    ageDivision: "10대 미만",
    ageItems: [
      "10대 미만",
      "10대",
      "20대",
      "30대",
      "40대",
      "50대",
      "60대 이상"
    ],
    jobDivision: "other",
    jobItems: [
      "other",
      "academic/educator",
      "artist",
      "clerical/admin",
      "college/grad student",
      "customer service",
      "doctor/health care",
      "executive/managerial",
      "farmer",
      "homemaker",
      "K-12 student",
      "lawyer",
      "programmer",
      "retired",
      "sales/marketing",
      "scientist",
      "self-employed",
      "technician/engineer",
      "tradesman/craftsman",
      "unemployed",
      "writer"
    ],
    picked: "",
    select: "gender"
  }),
  methods: {
    onSubmit: function() {
      let params = "";
      if (this.select == "gender") {
        params = {
          gender: this.genderDivision
        };
      } else if (this.select == "age") {
        params = {
          age: this.ageDivision.slice(0, 2)
        };
      } else if (this.select == "job") {
        parmas = {
          occupation: this.jobItems.indexOf(this.jobDivision)
        };
      }
      console.log(params);

      if (!params == "") this.submit(params);
    },

    clickGender: function() {
      return (this.select = "gender");
    },

    clickAge: function() {
      return (this.select = "age");
    },

    clickJob: function() {
      return (this.select = "job");
    }
  }
};
</script>