// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import * as VueGoogleMaps from 'vue2-google-maps'
import VueGeolocation from 'vue-browser-geolocation'
import App from './App'
import router from './router'

Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyBJhC_VA8gqutJ_6EI28GaAbMBbXVFeWqw'
  }
})

Vue.use(VueGeolocation)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
