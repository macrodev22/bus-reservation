<script setup>
import { onMounted, reactive, ref, computed } from 'vue';
import { useStore } from '../store';
import { makeReservation, getFare } from '../services/apiClient';
import { useToast } from 'vue-toastification';
import { useRouter } from 'vue-router';
import Card from '../components/Card.vue';
import Textfield from '../components/Textfield.vue';
import Title from '../components/Title.vue';
import Button from '../components/Button.vue';

const store = useStore()
const toast = useToast()
const router = useRouter()

const { reservation } = store

const booking = reactive({ ...reservation })
const passengerNames = ref(Array.from({ length: booking.numberOfSeats }, () => ''))
const unitFare = ref(0)
const fareLabel = ref('Total Fare (UGX)')
const totalFare = computed(() => unitFare.value * booking.numberOfSeats)


onMounted(() => {
    booking.origin = store.cities.find(city => city.value == booking.origin)?.data
    booking.destination = store.cities.find(city => city.value == booking.destination)?.data

    // Get fare for this route
    getFare({ origin: reservation.origin, destination: reservation.destination })
    .then(res => {
        unitFare.value = res.data.fare
        fareLabel.value = `Total Fare @ ${unitFare.value} (UGX)`
    })
    .catch(err => {
        toast.warning(`Error getting fares\n${err.message}`)
    })

})

const bookPassengers = () => {
    // TODO Validated names

    makeReservation({
        passengers: passengerNames.value,
        origin: reservation.origin,
        destination: reservation.destination
    }).then(
        res =>  {
            // console.log(res)
            // console.log(res.data)
            const { passengers } = res.data.data
            let msg = ''
            for(let passenger of passengers) msg += `‣ ${passenger} \n`
            // Clear the fields
            for(let i=0; i<passengerNames.value.length; i++) {
                passengerNames.value[i] = ''
            }
            toast(msg)
            toast.success(`Reservation added successfully`)
            router.push({ name: 'home' })
        }

    )
}

</script>
<template>
    <Card class="w-50">
        <Title>Make a reservation</Title>
        <Textfield label="Origin" :disabled="true" v-model="booking.origin" />
        <Textfield label="Destination" :disabled="true" v-model="booking.destination" />
        <Textfield label="Number of seats" type="number" disabled v-model="booking.numberOfSeats" />
        <Textfield :label="fareLabel" type="number" v-model="totalFare" disabled />
        <Textfield v-for="index in +booking.numberOfSeats" :label="`Passenger ${index} name`"
            :key="index" v-model="passengerNames[index-1]" />

        <div class="buttons">
            <Button class="primary" :onclick="bookPassengers">Reserve</Button>
        </div>
    </Card>
</template>