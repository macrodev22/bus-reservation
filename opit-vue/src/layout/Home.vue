<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import Card from '../components/Card.vue';
import Button from '../components/Button.vue';
import Title from '../components/Title.vue';
import Dropdown from '../components/Dropdown.vue';
import Textfield from '../components/Textfield.vue';
import { useStore } from '../store';
import { useToast } from 'vue-toastification';

const store = useStore()
const router = useRouter()
const toast = useToast()

const selectedOrigin = ref('')
const selectedDestination = ref('')
const numberOfSeats = ref('1')


const sendBooking = (e) => {

    // Validate
    if(!selectedOrigin.value || !selectedDestination.value) {
        toast.warning('The origin and destination are required!')
        return
    }

    if(numberOfSeats.value <= 0 || numberOfSeats.value > 20) {
        toast.warning('Invalid number of seats! \nSelect between 1 and 20 seats')
        return
    }

    e.preventDefault()
    const booking = { 
        numberOfSeats: numberOfSeats.value,
        origin: selectedOrigin.value,
        destination: selectedDestination.value
    }

    store.reserve(booking)

    router.push({ name: 'reserve' })
}

</script>
<template>
    <Card class="w-50">
        <Title>Make a reservation</Title>
        <Dropdown name="from" :options="store.cities" v-model="selectedOrigin" placeholder="Choose the Origin" />
        <Dropdown name="to" :options="store.cities":disable="selectedOrigin" v-model="selectedDestination" placeholder="Choose the destination" />
        <Textfield label="Number of seats" type="number" v-model="numberOfSeats" />
        <div class="buttons">
            <Button class="btn primary" :onclick="sendBooking">Book</Button>
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