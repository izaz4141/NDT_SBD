import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import store from './store'
import { createRouter, createWebHistory } from 'vue-router'
import HomePage from './views/HomePage.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      component: HomePage,
    },
    {
      path: '/about',
      component: () => import('./views/AboutPage.vue'),
    },
  ],
})

createApp(App).use(store).use(router).mount('#app')
