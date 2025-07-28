<script setup>
import HelloWorld from './components/HelloWorld.vue'
import Header_1 from './components/Header_1.vue'
import Chat_AI from './components/Chat_AI.vue'
import Chat from './components/Chat.vue'
import Items from './components/Items.vue'
import About from './components/About.vue'

</script>


<template>
  <Header_1 />
  <div id="app">
    <router-view />
  </div>
  <div>
    <a href="https://vite.dev" target="_blank">
      <img src="/vite.svg" class="logo" alt="Vite logo" />
    </a>
    <a href="https://vuejs.org/" target="_blank">
      <img src="./assets/vue.svg" class="logo vue" alt="Vue logo" />
    </a>
  </div>
  <HelloWorld msg="Vite + Vue" />

  
</template>

<script>
import Header from './components/Header_1.vue'

export default {
  name: 'App',
  components: {
    Header,
  },
}
</script>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
