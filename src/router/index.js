import Vue from 'vue'
import Router from 'vue-router'
import ItinGen from '@/components/ItinGen'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'ItinGen',
      component: ItinGen
    }
  ]
})
