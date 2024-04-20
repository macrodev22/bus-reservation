<script setup>
import { useStore } from '../store';
import { useRouter } from 'vue-router';
import { ref, onMounted } from 'vue';
import { updateFare, getFare } from '../services/apiClient';
import { useToast } from 'vue-toastification';
import Card from '../components/Card.vue';
import Title from '../components/Title.vue';
import Dropdown from '../components/Dropdown.vue';
import Textfield from '../components/Textfield.vue';
import Button from '../components/Button.vue';

const store = useStore()
const toast = useToast()
const router = useRouter()

onMounted(() => {
    if(!store.isAuthenticated) {
        router.push({ name: 'home' })
    }
})

const selectedOrigin = ref('')
const selectedDestination = ref('')
const fare = ref(0)

const getNewFare = () => {
    if(!selectedOrigin.value) return

    getFare({ origin: selectedOrigin.value, destination: selectedDestination.value })
    .then(res => {
            fare.value = res.data.fare
    })
    .catch(err => {
        toast.error(`Error getting fare\n${err.message}`)
    })
}

const storeNewFare = () => {
    updateFare({ origin: selectedOrigin.value, destination: selectedDestination.value, fare:fare.value })
    .then(res => {
        toast.success(`Fare added\n${res.data.message}`)
    })
    .catch(err => {
        toast.error(`Error updating fare\n${err.message}`)
    })
}

</script>
<template>
<Card class="w-50">
    <Title>Fares</Title>
    <Dropdown :options="store.cities" v-model="selectedOrigin" name="from" placeholder="Origin" />
    <Dropdown :options="store.cities" v-model="selectedDestination" name="to" placeholder="Destination" :disable="selectedOrigin" @change="getNewFare" />
    <Textfield label="Fare" v-model="fare" type="number" />
    <div class="buttons">
        <Button type="primary" :onclick="storeNewFare">Update</Button>
    </div>
</Card>
</template>