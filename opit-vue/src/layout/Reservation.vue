<script setup>
import { onMounted } from 'vue';
import { useStore } from '../store';
import Card from '../components/Card.vue';
import Textfield from '../components/Textfield.vue';
import Title from '../components/Title.vue';
import Dropdown from '../components/Dropdown.vue';

const store = useStore()

const { reservation } = store
const booking = { ...reservation }

onMounted(() => {

    booking.origin = store.cities.find(city => city.value == booking.origin)?.data
    booking.destination = store.cities.find(city => city.value == booking.destination)?.data
})


</script>
<template>
    <Card class="w-50">
        <Title>Make a reservation</Title>
        <Textfield label="Origin" disabled="true" v-model="booking.origin" />
        <Textfield label="Destination" disabled="true" v-model="booking.destination" />
        <Textfield label="Number of seats" type="number" v-model="booking.numberOfSeats" />
        <Textfield v-for="(pax, index) of store.reservation.numberOfSeats" :label="`Passenger ${index + 1} name`"
            :key="index" />
    </Card>
</template>