<script setup>
import { useRoute } from 'vue-router';

const route = useRoute();
</script>
<template>
    <div class="navigation">
        <div class="logo">
            <span>Opit Travellers</span>
        </div>
        <div>
            <RouterLink class="btn" :to="{ name: 'signin' }" :class="route.name == 'signin' ? 'primary': ''">Login</RouterLink>
            <RouterLink class="btn" :to="{ name: 'signup' }" :class="route.name == 'signup' ? 'primary': ''">Signup</RouterLink>
            <RouterLink :to="{ name: 'contacts' }" class="btn" :class="route.name == 'contacts' ? 'primary': ''">Contact Us</RouterLink>
            <RouterLink :to="{ name: 'home' }" class="btn" :class="route.name == 'home' ? 'primary': ''">Home</RouterLink>
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
        font-size: 2.5rem;
    }
}
</style>