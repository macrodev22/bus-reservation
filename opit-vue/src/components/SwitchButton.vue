<script setup>
import { RouterLink, useRoute } from 'vue-router';

const route = useRoute()

</script>
<template>
    <div class="btns-container">
        <div class="switch-btn">
            <RouterLink class="btn" :to="{ name: 'signin' }" :class="route.name == 'signin'? 'primary': ''">Log in</RouterLink>
            <RouterLink class="btn" :to="{ name: 'signup' }" :class="route.name == 'signup'? 'primary': ''">Sign up</RouterLink>
        </div>
    </div>
</template>
<style lang="scss">
.btns-container {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 3rem;
}
.switch-btn {
    border: 1px solid #33333312;
    width: max-content;
    border-radius: 3rem;
    padding: 0rem;

}
</style>