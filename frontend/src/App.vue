<script setup>
import HelloWorld from './components/HelloWorld.vue'
import Header_1 from './components/Header_1.vue'
// import HeaderMain from './components/Header.vue'
import Chat_AI from './components/Chat_AI.vue'
import Chat from './components/Chat.vue'
import Items from './components/Items.vue'
import About from './components/About.vue'

</script>


<template>
  <div id="app">
    <!-- <HeaderMain />  -->
    <Header_1 />
    <router-view />
  </div>
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
