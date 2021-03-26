import Vue from 'vue'
import VueRouter from 'vue-router'
import Books from './views/Books'

Vue.use(VueRouter)

export default new VueRouter ({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'books',
            component: Books,
        },
    ]
})