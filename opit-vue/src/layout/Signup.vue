<script setup>
import Card from '../components/Card.vue';
import Title from '../components/Title.vue';
import Button from '../components/Button.vue';
import Textinput from '../components/Textinput.vue';
import SwithButton from '../components/SwitchButton.vue';
</script>

<template>
    <Card class="w-50">
        <Title>Sign up</Title>
        <SwithButton />
        <Textinput placeholder="Username or email" />
        <Textinput type="password" placeholder="Password" />
        <Textinput type="password" placeholder="Confirm password" />
        <Textinput placeholder="Fullname" />
        <Textinput placeholder="Date of birth" type="date" />

        <div class="t-right">
            <Button type="primary">Register</Button>
        </div>
    </Card>
</template>