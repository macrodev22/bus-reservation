<script setup>
import { ref, onMounted } from 'vue';
import { getReservations, deleteReservation } from '../services/apiClient.js'
import { useToast } from 'vue-toastification';
import Card from '../components/Card.vue';
import Title from '../components/Title.vue';
import Button from '../components/Button.vue';

const reservations = ref([])
const toast = useToast()

onMounted(() => {
    // Get reservations
    getReservations()
    .then(res => {
        reservations.value = res.data.results
    })
    .catch(err => {
        toast.error('Error getting reservations, Ensure you are logged in')
    })

})

const removeReservationHandler = (id) => {
    deleteReservation(id)
    .then((res) => {
        toast.success(`Reservation ${res.data.data.id || ''} deleted successfully!`)

        getReservations()
        .then(res => {
        reservations.value = res.data.results
        })

    })
}

</script>
<template>
    <Card class="w-50">
        <Title>Manage Reservations</Title>
        <ul class="reservation-list">
            <li v-for="reservation in reservations" :key="reservation.reservation_id" >
                <div class="reservation">
                    <div class="pax">
                        {{ reservation.number_of_passengers }} Passengers
                        <p class="origin-destination">
                            {{ reservation.origin }} to {{ reservation.destination }}
                        </p>
                    </div>
                    <div class="names">
                        <ul>
                            <li class="name" v-for="passenger in reservation.passengers">{{ passenger }}</li>
                        </ul>
                    </div>
                    <div class="actions">
                        <Button :onclick="() => removeReservationHandler(reservation.reservation_id)">🗑 Delete</Button>
                    </div>
                </div>
            </li>
        </ul>
    </Card>
</template>
<style lang="scss">
.reservation-list {
    list-style-type: none;
    >li {
        display: block;
        &:nth-child(odd) {
            background-color: #d7d7d758;
        }
        .reservation {
            display: grid;
            grid-template-columns: 2fr 4fr 1fr;
            border-bottom: 1px solid #7b7b7b8b;
            margin-bottom: 1.5rem;
            background-color: transparent;

            &:hover {
                background-color: #c7383878;
            }
            .origin-destination {
                margin-top: 1rem;
                color: #ac0000d0;
            }
            .names {
                counter-reset: people;
                ul {
                    list-style-type: none;
                    .name {
                        margin-bottom: .5rem;
                    &::before {
                        counter-increment: people;
                        display: inline-block;
                        content: counter(people);
                        color: #1f3259;
                        margin-right: 1rem;

                    }
                }
                }
            }
            .actions {
                align-self: center;
                justify-self: center;
            }
        }
    }
}
</style>