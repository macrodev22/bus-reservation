<script setup>
import { useRoute, useRouter } from 'vue-router';
import { useStore } from '../store';
import apiClient from '../services/apiClient';

import Button from '../components/Button.vue';

const route = useRoute();
const store = useStore();
const router = useRouter();

const logUserOut = () => {
    store.auth.token = ''
    store.auth.user_id = null

    // Delete authorization headers
    delete apiClient.defaults.headers.common['Authorization']

    router.push({ name: 'home' })
}

</script>
<template>
    <div class="navigation">
        <div class="logo">
            <span>Opit Travellers</span>
        </div>
        <div>
            <RouterLink :to="{ name: 'home' }" class="btn" :class="route.name == 'home' ? 'primary': ''">Home</RouterLink>
            <Button :to="{ name: 'signin' }" v-if="store.isAuthenticated" :onclick="logUserOut">Logout</Button>
            <RouterLink class="btn" :to="{ name: 'manage_reservations' }" :class="route.name == 'manage_reservations' ? 'primary': ''" v-if="store.isAuthenticated">Reservations</RouterLink>
            <RouterLink class="btn" :to="{ name: 'signin' }" :class="route.name == 'signin' ? 'primary': ''" v-if="!store.isAuthenticated">Login</RouterLink>
            <RouterLink class="btn" :to="{ name: 'signup' }" :class="route.name == 'signup' ? 'primary': ''" v-if="!store.isAuthenticated">Signup</RouterLink>
            <RouterLink class="btn" :to="{ name: 'fares' }" :class="route.name == 'fares' ? 'primary': ''" v-if="store.isAuthenticated">Fares</RouterLink>
            <RouterLink :to="{ name: 'contacts' }" class="btn" :class="route.name == 'contacts' ? 'primary': ''">Contact Us</RouterLink>
            <slot />
        </div>
    </div>
</template>
<style>
.navigation {
    display: flex;
    justify-content: space-between;
    margin-bottom: 3rem;

    .logo {
        font-size: 4.5rem;
    }
}
</style>