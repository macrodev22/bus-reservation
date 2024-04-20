<script setup>
import { ref } from 'vue';
import { login } from '../services/apiClient';
import { useStore } from '../store';
import { useToast } from 'vue-toastification';
import { useRouter } from 'vue-router';
import apiClient from '../services/apiClient';
import Card from '../components/Card.vue';
import Title from '../components/Title.vue';
import Button from '../components/Button.vue';
import Textinput from '../components/Textinput.vue';
import SwithButton from '../components/SwitchButton.vue';

const username = ref('')
const password = ref('')

const toast = useToast()
const router = useRouter()

const store = useStore()

const logUserIn = () => {
    login({ username: username.value, password: password.value })
    .then(user_data => {
        const token = user_data.data.token

        store.auth.token = token

        // Add token to apiClient
        delete apiClient.defaults.headers.common['Authorization']
        apiClient.defaults.headers.common['Authorization'] = `Bearer ${token}`

        router.push({ name:'fares' })

    })
    .catch(err => {
        toast.warn(`Error logging in\n${err.message}`)
    }) 

}

</script>

<template>
    <Card class="w-50">
        <Title>Sign in</Title>
        <SwithButton />
        <Textinput placeholder="Username or email" v-model="username" />
        <Textinput type="password" placeholder="Password" v-model="password" />
        <div class="t-right">
            <a>Forgot password?</a>
            <Button type="primary" :onclick="logUserIn">Login</Button>
        </div>
    </Card>
</template>