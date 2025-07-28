<template>
    <header>
        <div class="header-container">
            <NavLeft />
            <NavCenter />
            <NavRight />
        </div>
    </header>
</template>


<script setup>
import NavLeft from './Header/nav-left.vue'
import NavCenter from './Header/nav-center.vue'
import NavRight from './Header/nav-right.vue'
</script>

<style scoped>
header {
    width: 100vw;
    position: relative;
    left: 50%;
    right: 50%;
    margin-left: -50vw;
    margin-right: -50vw;
    background-color: #04004b;
    padding: 1rem 2rem;
    box-sizing: border-box;
}
/* Внутренний контейнер для центрирования контента внутри header */
.header-container {
    max-width: 1280px;
    margin: 0 auto;
    display: flex;
    align-items: center;
    justify-content: space-between;
}
</style>
