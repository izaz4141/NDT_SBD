import { createRouter, createWebHistory } from 'vue-router'
import { links } from '../data/dummy'
import NotFound from '../views/NotFound.vue'
import LoginPage from '../views/LoginPage.vue'
import RegisterPage from '../views/RegisterPage.vue'
// route rendered statically because gh-pages cant get file after build
const routee = []
links.map((category) => {
  category.children.map((link) =>
    routee.push({
      name: link.name,
      path: link.url,
      component: () => link.component,
    }),
  )
})

routee.push(
  {
    name: 'login',
    path: '/login',
    component: LoginPage,
  },
  {
    name: 'register',
    path: '/register',
    component: RegisterPage,
  },
  {
    name: 'not-found',
    path: '/:pathMatch(.*)*',
    component: NotFound,
  },
  {
    name: 'bad-not-found',
    path: '/:pathMatch(.*)',
    component: NotFound,
  },
)

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routee,
})

export default router
