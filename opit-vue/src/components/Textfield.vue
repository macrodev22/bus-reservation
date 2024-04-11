<script setup>
import { ref, defineModel } from 'vue'

const props = defineProps({
    type:{
        type:String,
        default:'text'
    },
    name:String,
    label: String,
    modelValue:String,
    disabled: {
        type: Boolean,
        default:false
    },
    value:String
})

const emit = defineEmits(['update:modelValue'])
const value = defineModel()

</script>

<template>
        <div class="input-text">
        <label :for="name"> {{ label }}</label>
        <input :type="type" :name="name" :id="name" :value="value" class="input" v-model="value" @change="emit('update:modelValue', value)" :disabled="disabled" />
    </div>
</template>

<style lang="scss">
.input-text {
    display: flex;
    justify-content: space-between;
    margin-bottom: 2rem;

    label {
        flex: 0 0 25%;
    }
}

</style>
