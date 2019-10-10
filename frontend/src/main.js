import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import router from './router'
import store from './store'
import 'expose-loader?$!expose-loader?jQuery!jquery'
import IMP from 'vue-iamport'

Vue.config.productionTip = false
Vue.use(IMP, 'imp20223819')
Vue.IMP().load()

new Vue({
  vuetify,
  router,
  store,
  render: h => h(App)
}).$mount('#app')
