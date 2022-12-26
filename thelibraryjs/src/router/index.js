import { createWebHistory, createRouter } from "vue-router"
import BooksIndex from '@/views/Books/Index'
import Dashboard from '@/views/Index'

const routes = [
    {
        path: '/',
        component: Dashboard
    },
    {
        path: '/books',
        component: BooksIndex,
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router