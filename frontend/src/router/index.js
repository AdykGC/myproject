import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/HelloWorld.vue'
import Chat_AI from '../components/Chat_AI.vue'
import Chat from '../components/Chat.vue'
import Items from '../components/Items.vue'
import About from '../components/About.vue'
import Chat_With_Micro from '../components/Chat_With_Micro.vue'

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/items', name: 'Items', component: Items },
  { path: '/chat_ai', name: 'Chat_AI', component: Chat_AI },
  { path: '/chat', name: 'Chat', component: Chat },
  { path: '/chat_with_micro', name: 'Chat_With_Micro', component: Chat_With_Micro },
  { path: '/about', name: 'About', component: About },
  { path: '/about', name: 'About', component: About },
  { path: '/about', name: 'About', component: About },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
