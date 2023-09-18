 # 【vue3】動的に生成した DOM 要素に css を適用する
 ## 概要
 動的に生成した \<li\> 要素のうち、特定の要素にだけ css を適用したい

 ## v-bind:class を使用して、css を適用したい要素に class を付与する
 以下の例では、表示中のページ番号に対してのみ css を適用している

```vue
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
```