<script setup>
import { ref } from 'vue';
import { useToast } from 'vue-toastification';
import { registerUser } from '../services/apiClient';
import Card from '../components/Card.vue';
import Title from '../components/Title.vue';
import Button from '../components/Button.vue';
import Textinput from '../components/Textinput.vue';
import SwithButton from '../components/SwitchButton.vue';

const toast = useToast()

const userForm = ref({
    username:'',
    password: '',
    passwordConfirmation: '',
    fullname: '',
    dateOfBirth: ''
})


const registerUserDetails = (e) => {
    e.preventDefault();
    // Validate 
    if((userForm.value.fullname == '' || userForm.value.password == '' || userForm.value.passwordConfirmation == '' || userForm.value.username == '' || userForm.value.dateOfBirth == '')) {
        toast.warning('All fields are mandatory!')
        return
    }

    if(userForm.value.password !== userForm.value.passwordConfirmation) {
        toast.error('Password and Password Confirmation do not match!')
        return
    }
     
    // Register the user
    registerUser(userForm.value)
    .then(res => {
        toast('User created succesfully')
    })
    .catch(err => {
        toast.error(`Error creating user!\n${err.message}`)
        console.log('Error registring User', err.message)
    })
}
</script>

<template>
    <Card class="w-50">
        <Title>Sign up</Title>
        <SwithButton />
        <Textinput placeholder="Username or email" v-model="userForm.username" />
        <Textinput type="password" placeholder="Password" v-model="userForm.password" />
        <Textinput type="password" placeholder="Confirm password" v-model="userForm.passwordConfirmation" />
        <Textinput placeholder="Fullname" v-model="userForm.fullname" />
        <Textinput placeholder="Date of birth" type="date" v-model="userForm.dateOfBirth" />

        <div class="t-right">
            <Button type="primary" :onclick="registerUserDetails">Register</Button>
        </div>
    </Card>
</template>