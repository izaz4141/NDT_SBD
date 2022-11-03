import { createRouter, createWebHistory } from 'vue-router'
import { links } from '../data/dummy'

const routee = []
links.map((category) => {
  category.children.map((link) =>
    routee.push({
      name: link.name,
      path: link.url,
      component: () => import(link.component),
    }),
  )
})

routee.push(
  {
    name: 'not-found',
    path: '/:pathMatch(.*)*',
    component: () => import('../views/NotFound.vue'),
  },
  {
    name: 'bad-not-found',
    path: '/:pathMatch(.*)',
    component: () => import('../views/NotFound.vue'),
  },
)

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routee,
})

export default router
