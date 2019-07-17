import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/components/Main'
import File from '@/components/File'
import Search from '@/components/Search'
import Auth from '@/components/Auth'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path:'/Auth',
      name:'Auth',
      component: Auth
    },
    {
      path: '/',
      name: 'fileup',
      component: File
    },
    {
      path: '/Main',
      name: 'Main',
      component: Main
    },
    {
      path: '/Search',
      name: 'Search',
      component: Search
    }
  ]
})
