<template>
  <v-layout>
    <v-dialog v-model="dialog" max-width="500">
      <template v-slot:activator="{ on }">
        <v-btn v-on="on">
          <v-icon>perm_identity</v-icon>
        </v-btn>
      </template>

      <v-card>
        <v-card-title class="headline">Login</v-card-title>
        <v-card-text>
          <v-container grid-list-md>
            <v-layout column wrap>
              <v-form ref="form" v-model="valid" lazy-validation>
                <v-text-field v-model="data.user_id" :rules="idRules" label="ID" required></v-text-field>

                <v-text-field
                  v-model="data.user_pw"
                  :append-icon="show ? 'visibility' : 'visibility_off'"
                  :rules="pwRules"
                  :type="show ? 'text' : 'password'"
                  label="Password"
                  @click:append="show = !show"
                  required
                ></v-text-field>
              </v-form>
            </v-layout>
          </v-container>

          <small>*indicates required field</small>
        </v-card-text>

        <br />

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue" @click="submit">Login</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-layout>
</template>

<script>
import { mapActions } from "vuex";

export default {
  data() {
    return {
      valid: true,
      dialog: false,
      idRules: [v => !!v || "ID is required"],
      pwRules: [v => !!v || "Password is required"],
      show: false,
      data: {
        user_id: "",
        user_pw: ""
      }
    };
  },
  methods: {
    ...mapActions("data", ["Login"]),
    async submit() {
      console.log("dd");

      if (this.$refs.form.validate()) {
        console.log("ddd");
        console.log(this.data);

        await this.Login(this.data);
        console.log("ddddd");

        this.dialog = false;
      }
    },
    reset() {
      this.$refs.form.reset();
    }
  },
  watch: {
    dialog: function() {
      this.reset();
    }
  }
};
</script>

<style>
.headline {
  padding-bottom: 50px;
}

.modalface {
  width: 100%;
}

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
