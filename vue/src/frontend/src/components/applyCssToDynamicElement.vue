<script setup>
import { ref } from 'vue'
const currentPage = ref(1)
const pageCount = ref(10)
</script>

<template>
   <ul class="paging-footer">
     <li v-for="page in pageCount" :key="page" class="paging-item" :class="{selectedItem : page === currentPage}">
        <button @click="currentPage = page" class="paging-button">{{ page }}</button>
     </li>
   </ul>
</template>

<style>
.paging-footer {
  display: flex;
  justify-content: center;
  list-style: none;
}

.selectedItem>.paging-button {
  background-color: #ff5733;
  color: white;
} 

</style>