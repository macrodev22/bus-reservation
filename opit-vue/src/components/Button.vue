<template>
    <button class="btn" :class="props.type == 'primary'? 'primary' : ''">
        <slot />
    </button>
</template>

<style lang="scss">
.btn {
    &, &:link, &:visited {
        font-size: 2rem;
        border-radius: 3rem;
        padding: 1rem 3rem;
        display: inline-block;
        margin: 0.5rem 1rem;
        text-decoration: none;
        cursor: pointer;
        color: #fe7575;
        background-color: #fff;
        border: none;
        &.primary { 
            background-color: #fe7575;
            color: #fff;
            &:hover {
                background-color: #e15353;
            }
        }
        &:hover {
            background-color: #eee;
        }
    }
}


</style>
<script setup>
const props = defineProps({
    type: {
        type: String,
        default: '',
    }
})

</script>