<template>
    <div class="nav-left">
        <!-- Main -->
        <router-link to="/" class="icon-link">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" viewBox="0 0 256 256">
                <path d="M216,40H40A16,16,0,0,0,24,56V200a16,16,0,0,0,16,16H216a16,16,0,0,0,16-16V56A16,16,0,0,0,216,40Zm0,16V88H40V56Z"></path>
            </svg>
        </router-link>
        <!-- Shop merch -->
        <router-link to="/items" class="icon-link">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="currentColor" class="size-6" viewBox="0 0 24 24" >
                <path fill-rule="evenodd" d="M5.25 2.25a3 3 0 0 0-3 3v4.318a3 3 0 0 0 .879 2.121l9.58 9.581c.92.92 2.39 1.186 3.548.428a18.849 18.849 0 0 0 5.441-5.44c.758-1.16.492-2.629-.428-3.548l-9.58-9.581a3 3 0 0 0-2.122-.879H5.25ZM6.375 7.5a1.125 1.125 0 1 0 0-2.25 1.125 1.125 0 0 0 0 2.25Z" clip-rule="evenodd" />
            </svg>
            <span>Shop merch</span>
        </router-link>
        <!-- Bug report -->
        <router-link to="/about" class="icon-link">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" viewBox="0 0 256 256">
                <path d="M224,120H208V104h16a8,8,0,0,1,0,16ZM32,104a8,8,0,0,0,0,16H48V104Zm176,56c0,2.7-.14,5.37-.4,8H224a8,8,0,0,1,0,16H204.32a80,80,0,0,1-152.64,0H32a8,8,0,0,1,0-16H48.4c-.26-2.63-.4-5.3-.4-8v-8H32a8,8,0,0,1,0-16H48V120H208v16h16a8,8,0,0,1,0,16H208Zm-72-16a8,8,0,0,0-16,0v64a8,8,0,0,0,16,0ZM69.84,57.15A79.76,79.76,0,0,0,48.4,104H207.6a79.76,79.76,0,0,0-21.44-46.85l19.5-19.49a8,8,0,0,0-11.32-11.32l-20.29,20.3a79.74,79.74,0,0,0-92.1,0L61.66,26.34A8,8,0,0,0,50.34,37.66Z"></path>
            </svg>
            <span>Report a bug</span>
        </router-link>
    </div>
</template>

<style scoped>
.nav-left, .nav-center, .nav-right {
    display: flex;
    align-items: center;
    gap: 15px;
}

nav a, .icon-link {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    text-transform: uppercase;
    text-decoration: none;
    color: #ffffff;
}

.icon-link:hover {
    color: #007bff;
    text-decoration: underline;
}
</style>
