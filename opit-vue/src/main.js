import { createApp } from 'vue'
import './style.scss'
import Toast from 'vue-toastification'
import App from './App.vue'
import { createPinia } from 'pinia'
import router from './router'

import 'vue-toastification/dist/index.css'
import 'animate.css'

const toastOptions = {
    transition: "Vue-Toastification__bounce",
    maxToasts: 20,
    newestOnTop: true
  }

const pinia = createPinia()

createApp(App)
.use(pinia)
.use(router)
.use(Toast, toastOptions)
.mount('#app')
