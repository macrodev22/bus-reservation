<script setup>
import Navigation from './layout/Navigation.vue';
import { RouterView } from 'vue-router';
import { useStore } from './store';

const store = useStore()

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
