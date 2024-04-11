<template>
    <div class="input-drop">
        <label :for="name"> {{ capitalize(props.name) }}</label>
        <select :name="name" :id="name" v-model="value" @change="emit('update:modelValue', value)">
            <option v-if="placeholder" selected disabled value="">{{ placeholder }}</option>
            <option v-for="(opt, index) of props.options" :key="index" :value="opt.value" :disabled="disable == opt.value ? true:false" >{{ opt.data }}</option>
        </select>
    </div>
</template>
<script setup>
import { ref, defineModel } from 'vue'
const props = defineProps({
    name: String,
    modelValue:String,
    options: {
        type:Array,
        required:true,
    },
    disable: {
        type:String,
        default:''
    },
    placeholder: {
        type: String,
        default:''
    },
})

const emit = defineEmits(['update:modelValue'])

const value = defineModel()


const capitalize = text => text[0].toUpperCase() + text.slice(1)

</script>

<style lang="scss">
.input-drop {
    display: flex;
    gap: 1rem;
    justify-content: space-between;
    margin-bottom: 1rem;

    label {
        flex: 0 0 25%;
        justify-self: flex-start;
    }
    select {
        flex: 1;
        font-size: inherit;
        padding: .5rem 1rem;
        font-style: italic;
    }
}

</style>