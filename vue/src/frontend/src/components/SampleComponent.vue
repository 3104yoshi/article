<script setup>
import { ref, computed } from 'vue'
const x = ref(1)
const calculate_with_ref = ref(x.value)
const calculate_with_computed = computed(() => x.value) //算出プロパティの定義
</script>

<template>
  <div>
    <button @click="x++">x is {{ x }}</button>
    <p>ref : {{ calculate_with_ref }}</p>
    <p>computed : {{ calculate_with_computed }}</p>
  </div>
</template>