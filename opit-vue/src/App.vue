<script setup>
import Navigation from './layout/Navigation.vue';
import { RouterView } from 'vue-router';


</script>

<template>
  <Navigation>
  </Navigation>
  <div>
    <RouterView />
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
