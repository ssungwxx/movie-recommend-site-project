
import Vue from "vue";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
import Vuetify from "vuetify";
import "vuetify/dist/vuetify.min.css";
import 'expose-loader?$!expose-loader?jQuery!jquery'
import IMP from 'vue-iamport'
import router from "./router";
import store from "./store";


Vue.config.productionTip = false
Vue.use(IMP, 'imp20223819')
Vue.IMP().load()
new Vue({
  Vuetify,
  vuetify,
  router,
  store,
  render: h => h(App)
}).$mount("#app");
