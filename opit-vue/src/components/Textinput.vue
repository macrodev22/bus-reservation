<script setup>
const props = defineProps({
    placeholder: String,
    modelValue: String,
    type: {
        type:String,
        default:'text'
    }
})

const value = defineModel()
const emit = defineEmits(['update:modelValue'])

</script>
<template>
<div class="text-input">
    <input :type="type" :placeholder="placeholder" v-model="value" @change="emit('update:modelValue', $event.target.value)" />
    <label>{{ placeholder }}</label>
</div>
</template>

<style lang="scss">
.text-input {
    margin-bottom: 3.5rem;
    position: relative;

    label {
        position: absolute;
        color: #0f6cb8;
        transition: all .2s;
        font-size: .7em;
        top: -1rem;
        left: 1rem;

    }

    input {
        border: none;
        border-bottom: 1px solid #33333345;
        font-family: inherit;
        padding: .5rem 1rem;
        font-style: italic;
        font-size: inherit;
        width: 100%;
        &:focus {
            outline: none;
            border-bottom: 2px solid #000000ee;
        }
        &:placeholder-shown {
            &~label {
                opacity: 0;
            }
        }
    }
}
</style>