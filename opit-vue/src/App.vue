<script setup>
import Navigation from './layout/Navigation.vue';
import apiClient from './services/apiClient';
import { RouterView } from 'vue-router';
import { onMounted } from 'vue';
import { useStore } from './store';

const store = useStore()

//Fetch Cities
onMounted(() => {
        apiClient.get('/cities')
        .then(res => {
          const dbCities = res.data

          const cityData = dbCities.map(city => { return {data: city['name'] , value: city['city_id']} })

          store.cities = cityData
        })
        .catch(err => {
          console.log(`Error fetching cities `, err.message)

        })
        
})


</script>

<template>
  <Navigation>
  </Navigation>
  <div>
    <RouterView v-slot="{ Component }">
      <Transition mode="out-in" enter-active-class="animate__animated animate__bounceInRight" leave-active-class="animate__animated animate__bounceOutLeft">
       <component :is="Component" />
      </Transition>
    </RouterView>
  </div>
  <div class="bus-bg"></div>
</template>

<style scoped>


.bus-bg {
  background: url('assets/bus.png');
  background-size: cover;
  min-height: 30rem;
  min-width: 50rem;
  position: fixed;
  bottom: 0;
  right: 0;
}


</style>
