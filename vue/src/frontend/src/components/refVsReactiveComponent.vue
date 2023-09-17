<script setup>
import { reactive, ref } from 'vue'

const array = ["a", "b"]

const ref_primitive = ref(1)
const ref_object = ref(array)
const reactive_primitive = reactive(1) //value cannot be made reactive: 1
const reactive_object = reactive(array) // ok

console.log(ref_primitive.value === 1)
console.log(ref_object.value === array)
console.log(reactive_primitive === 1)
console.log(reactive_object === array)

</script>

<template>
  <div>
    <button @click="ref_primitive++">ref_primitive</button>
    <p>ref_primitive : {{ ref_primitive }}</p>
    <button @click="ref_object.push('push!')">ref_object</button>
    <p>ref_object : {{ ref_object }}</p>
    <button @click="reactive_primitive++">reactive_primitive</button>
    <p>reactive_primitive : {{ reactive_primitive }}</p>
    <button @click="reactive_object.push('push!')">reactive_object</button>
    <p>reactive_object : {{ reactive_object }}</p>
<!-- クリックで値を変更しても反映されない -->
    <button @click="array.push('push'); console.log(array);">array push</button>
  </div>
</template>