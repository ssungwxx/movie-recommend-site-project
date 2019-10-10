<template>
  <v-layout row justify-center>
    <v-dialog v-model="dialog" max-width="600px">
      <template v-slot:activator="{ on }">
        <v-btn v-on="on">
          <v-icon>person_add</v-icon>
        </v-btn>
      </template>

      <v-card>
        <v-card-title>
          <span class="headline">SignUp</span>
        </v-card-title>
        <v-card-text>
          <v-container grid-list-md>
            <v-layout column wrap>
              <v-form ref="form" v-model="valid" lazy-validation>
                <v-text-field v-model="user.User" :rules="userRules" label="User*" required></v-text-field>

                <v-text-field v-model="user.Age" :rules="ageRules" label="Age*" required></v-text-field>

                <v-select
                  v-model="user.Gender"
                  :items="genders"
                  :rules="genderRules"
                  label="Gender*"
                  required
                ></v-select>

                <v-select
                  v-model="user.Occupation"
                  :items="occupations"
                  :rules="occupationRules"
                  label="occupation*"
                  required
                ></v-select>
              </v-form>
            </v-layout>
          </v-container>
          <small>*indicates required field</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="close">Close</v-btn>
          <v-btn color="blue darken-1" text @click="reset">Reset</v-btn>
          <v-btn :disabled="!valid" color="blue darken-1" text @click="submit">Submit</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-layout>
</template>

<script>
import api from "../api/index";

export default {
  data() {
    return {
      valid: true,
      dialog: false,
      genders: ["M", "F"],
      occupations: [
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
      userRules: [v => !!v || "User name is required"],
      ageRules: [
        v => !!v || "Age is required",
        v => /^[0-9]*$/.test(v) || "Age must be valid"
      ],
      genderRules: [v => !!v || "Gender is required"],
      occupationRules: [v => !!v || "Occupation is required"],
      user: {
        User: "",
        Age: "",
        Gender: "",
        Occupation: ""
      }
    };
  },
  watch: {
    dialog() {
      this.reset();
    }
  },
  methods: {
    async submit() {
      if (this.$refs.form.validate()) {
        const resp = await api.signup(this.user);
        if (resp.status == 201) {
          alert("Signed up!");
          this.reset();
          this.dialog = false;
        } else {
          alert("Check your form again!");
        }
      }
    },
    reset() {
      this.$refs.form.reset();
    },
    close() {
      this.$refs.form.reset();
      this.dialog = false;
    }
  }
};
</script>

<style>
@media screen and (max-width: 599px) {
  .headerButton {
    display: none;
  }
}

@media screen and (min-width: 600px) {
  .sidebarButton {
    display: none;
  }
}
</style>
