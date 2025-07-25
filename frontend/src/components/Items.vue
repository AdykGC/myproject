<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const items = ref([])

onMounted(() => {
  axios.get(`${import.meta.env.VITE_API_URL}/items/`)
    .then(res => {
      items.value = res.data
    })
})
</script>

<template>
  <div>
    <h1>Items from Django</h1>
    <ul class="item-list">
      <li v-for="item in items" :key="item.id">{{ item.name }}</li>
    </ul>
  </div>
</template>


<style scoped>
.item-list {
  list-style-type: none; /* Убираем точки */
  padding-left: 0;        /* Убираем отступ */
}
</style>