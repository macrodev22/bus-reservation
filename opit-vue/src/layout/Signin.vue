<script setup>
import Card from '../components/Card.vue';
import Title from '../components/Title.vue';
import Button from '../components/Button.vue';
import Textinput from '../components/Textinput.vue';
import SwithButton from '../components/SwitchButton.vue';
</script>

<template>
    <Card class="w-50">
        <Title>Sign in</Title>
        <SwithButton />
        <Textinput placeholder="Username or email" />
        <Textinput type="password" placeholder="Password" />
        <div class="t-right">
            <a>Forgot password?</a>
            <Button type="primary">Login</Button>
        </div>
    </Card>
</template>