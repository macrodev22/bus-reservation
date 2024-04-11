<script setup>
import Card from '../components/Card.vue';
import Title from '../components/Title.vue';
</script>

<template>
<Card class="w-50">
<Title>About Us</Title>

<div class="contacts">
    <p>Phone: +256 712 345 678</p>
    <p>Website: www.opitravellers.com</p>
</div>
</Card>
</template>
<style lang="scss">
.contacts {
    margin: 5rem 0;
    p {
        line-height: 5rem;
    }
}
</style>