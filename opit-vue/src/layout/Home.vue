<script setup>
import { ref } from 'vue';
import Card from '../components/Card.vue';
import Button from '../components/Button.vue';
import Title from '../components/Title.vue';
import Dropdown from '../components/Dropdown.vue';
import Textfield from '../components/Textfield.vue';
import { useStore } from '../store';

const store = useStore()

const selectedOrigin = ref('')
const destination = ref('')
const numberOfSeats = ref('1')

const optionSelected = e => {
    selectedOrigin.value = e.target.value;

}

const sendBooking = (e) => {
    // console.log('Booking with:', selectedOrigin.value, destination.value, numberOfSeats.value)
    const booking = { 
        numberOfSeats: numberOfSeats.value,
        origin: selectedOrigin.value,
        destination: destination.value
    }

    store.reservation = { ...booking }

}

</script>
<template>
    <Card class="w-50">
        <Title>Make a reservation</Title>
        <Dropdown name="from" :options="store.cities" :onchange="optionSelected" v-model="selectedOrigin" placeholder="Choose the Origin" />
        <Dropdown name="to" :options="store.cities" :disable="selectedOrigin" placeholder="Choose the destination" v-model="destination" />
        <Textfield label="Number of seats" type="number" v-model="numberOfSeats" />
        <div class="buttons">
            <RouterLink class="btn primary" :to="{ name: 'reserve' }" :onclick="sendBooking">Book</RouterLink>
            <Button class="primary">Send a parcel</Button>
            <Button class="primary">Bus Schedule</Button>
            <Button class="primary">Internal Facilities</Button>
        </div>
    </Card>

</template>

<style lang="scss">
.buttons {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    margin-top: 2rem;
}
</style>