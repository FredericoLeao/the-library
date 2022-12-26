import { createWebHistory, createRouter } from "vue-router"
import BooksIndex from '@/views/Books/Index'
import AuthorsIndex from '@/views/Authors/Index'
import Dashboard from '@/views/Index'

const routes = [
    {
        path: '/',
        component: Dashboard
    },
    {
        path: '/books',
        component: BooksIndex,
    },
    {
        path: '/authors',
        component: AuthorsIndex,
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router