<script setup>
import Header from './components/Header.vue'
import Chat_With_Micro from './components/Chat_With_Micro.vue'
</script>


<template>
  <div id="app">
    <Chat_With_Micro />
  </div>
</template>

<script>

export default {
  name: 'App',
  components: {
    Header,
  },
}
</script>
