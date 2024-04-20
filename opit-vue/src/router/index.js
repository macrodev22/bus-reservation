import { createRouter, createWebHashHistory } from "vue-router";
import Home from "../layout/Home.vue";
import Signin from "../layout/Signin.vue";
import Signup from "../layout/Signup.vue"
import Contacts from "../layout/Contacts.vue";
import Reservation from "../layout/Reservation.vue";
import Fares from "../layout/Fares.vue";
import ReservationsManager from '../layout/ReservationsManager.vue'


const routes = [
    {
        path: '/',
        component: Home,
        name: 'home'
    },
    {
        path: '/signin',
        component: Signin,
        name: 'signin'
    },
    {
        path: '/signup',
        component: Signup,
        name: 'signup'
    },    
    {
        path: '/contacts',
        component: Contacts,
        name: 'contacts'
    },
    {
        path: '/reserve',
        component: Reservation,
        name: 'reserve'
    },
    {
        path: '/fares',
        component: Fares,
        name: 'fares',
        meta: {
            authRequired: true
        }
    },
    {
        path: '/reservations',
        component: ReservationsManager,
        name: 'manage_reservations',
        meta: {
            authRequired: true
        }
    },
]

const router = createRouter({
    routes,
    history: createWebHashHistory(),
})

export default router