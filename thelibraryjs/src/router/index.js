import { createWebHistory, createRouter } from "vue-router"

const routes = [
    // {
    //     path: '/',
    //     component: Dashboard
    // },
    //{
    //    path: '/books',
    //    component: Books,
    //}
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router