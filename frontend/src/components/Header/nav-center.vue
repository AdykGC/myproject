<template>
    <div class="nav-center">
        <!-- Support -->
        <router-link to="/chat_ai" class="icon-link">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="size-6" viewBox="0 0 24 24" >
                <path fill-rule="evenodd" d="M8.25 6.75a3.75 3.75 0 1 1 7.5 0 3.75 3.75 0 0 1-7.5 0ZM15.75 9.75a3 3 0 1 1 6 0 3 3 0 0 1-6 0ZM2.25 9.75a3 3 0 1 1 6 0 3 3 0 0 1-6 0ZM6.31 15.117A6.745 6.745 0 0 1 12 12a6.745 6.745 0 0 1 6.709 7.498.75.75 0 0 1-.372.568A12.696 12.696 0 0 1 12 21.75c-2.305 0-4.47-.612-6.337-1.684a.75.75 0 0 1-.372-.568 6.787 6.787 0 0 1 1.019-4.38Z" clip-rule="evenodd" />
                <path d="M5.082 14.254a8.287 8.287 0 0 0-1.308 5.135 9.687 9.687 0 0 1-1.764-.44l-.115-.04a.563.563 0 0 1-.373-.487l-.01-.121a3.75 3.75 0 0 1 3.57-4.047ZM20.226 19.389a8.287 8.287 0 0 0-1.308-5.135 3.75 3.75 0 0 1 3.57 4.047l-.01.121a.563.563 0 0 1-.373.486l-.115.04c-.567.2-1.156.349-1.764.441Z" />
            </svg>
            <span>Support</span>
        </router-link>
        <!-- Community -->
        <router-link to="/chat" class="icon-link">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" viewBox="0 0 256 256">
                <path d="M230.4,219.19A8,8,0,0,1,224,232H32a8,8,0,0,1-6.4-12.8A67.88,67.88,0,0,1,53,197.51a40,40,0,1,1,53.93,0,67.42,67.42,0,0,1,21,14.29,67.42,67.42,0,0,1,21-14.29,40,40,0,1,1,53.93,0A67.85,67.85,0,0,1,230.4,219.19ZM27.2,126.4a8,8,0,0,0,11.2-1.6,52,52,0,0,1,83.2,0,8,8,0,0,0,12.8,0,52,52,0,0,1,83.2,0,8,8,0,0,0,12.8-9.61A67.85,67.85,0,0,0,203,93.51a40,40,0,1,0-53.93,0,67.42,67.42,0,0,0-21,14.29,67.42,67.42,0,0,0-21-14.29,40,40,0,1,0-53.93,0A67.88,67.88,0,0,0,25.6,115.2,8,8,0,0,0,27.2,126.4Z"></path>
            </svg>
            <span>Community</span>
        </router-link>
        <!-- Social media -->
        <router-link to="/chat_with_micro" class="icon-link">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" viewBox="0 0 256 256"><path d="M80,120v16a16,16,0,0,1-16,16V104A16,16,0,0,1,80,120ZM248,72V184a16,16,0,0,1-16,16H24A16,16,0,0,1,8,184V72A16,16,0,0,1,24,56H232A16,16,0,0,1,248,72ZM96,120A32,32,0,0,0,64,88H56a8,8,0,0,0-8,8v64a8,8,0,0,0,8,8h8a32,32,0,0,0,32-32Zm32,0V104h16a8,8,0,0,0,0-16H120a8,8,0,0,0-8,8v64a8,8,0,0,0,8,8h24a8,8,0,0,0,0-16H128V136h8a8,8,0,0,0,0-16Zm82.17-31.7a8,8,0,0,0-9.87,5.53L190,130.45,179.7,93.83a8,8,0,0,0-15.4,4.34l18,64a8,8,0,0,0,15.4,0l18-64A8,8,0,0,0,210.17,88.3Z"></path></svg>
        </router-link>
        <router-link to="/about" class="icon-link">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" viewBox="0 0 256 256"><path d="M232,128a104.16,104.16,0,0,1-91.55,103.26,4,4,0,0,1-4.45-4V152h24a8,8,0,0,0,8-8.53,8.17,8.17,0,0,0-8.25-7.47H136V112a16,16,0,0,1,16-16h16a8,8,0,0,0,8-8.53A8.17,8.17,0,0,0,167.73,80H152a32,32,0,0,0-32,32v24H96a8,8,0,0,0-8,8.53A8.17,8.17,0,0,0,96.27,152H120v75.28a4,4,0,0,1-4.44,4A104.15,104.15,0,0,1,24.07,124.09c2-54,45.74-97.9,99.78-100A104.12,104.12,0,0,1,232,128Z"></path></svg>
        </router-link>
        <router-link to="/about" class="icon-link">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" viewBox="0 0 256 256"><path d="M176,24H80A56.06,56.06,0,0,0,24,80v96a56.06,56.06,0,0,0,56,56h96a56.06,56.06,0,0,0,56-56V80A56.06,56.06,0,0,0,176,24ZM128,176a48,48,0,1,1,48-48A48.05,48.05,0,0,1,128,176Zm60-96a12,12,0,1,1,12-12A12,12,0,0,1,188,80Zm-28,48a32,32,0,1,1-32-32A32,32,0,0,1,160,128Z"></path></svg>
        </router-link>
        <router-link to="/about" class="icon-link">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" viewBox="0 0 256 256"><path d="M216,24H40A16,16,0,0,0,24,40V216a16,16,0,0,0,16,16H216a16,16,0,0,0,16-16V40A16,16,0,0,0,216,24ZM96,176a8,8,0,0,1-16,0V112a8,8,0,0,1,16,0ZM88,96a12,12,0,1,1,12-12A12,12,0,0,1,88,96Zm96,80a8,8,0,0,1-16,0V140a20,20,0,0,0-40,0v36a8,8,0,0,1-16,0V112a8,8,0,0,1,15.79-1.78A36,36,0,0,1,184,140Z"></path></svg>
        </router-link>
        <router-link to="/about" class="icon-link">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" viewBox="0 0 256 256"><path d="M200,24H56A16,16,0,0,0,40,40V216a16,16,0,0,0,16,16H200a16,16,0,0,0,16-16V40A16,16,0,0,0,200,24ZM136,200a8,8,0,0,1-16,0V160a8,8,0,0,1,16,0Zm48-80H147.31l26.35,26.34a8,8,0,0,1-11.32,11.32L128,123.31,93.66,157.66a8,8,0,0,1-11.32-11.32L108.69,120H72a8,8,0,0,1,0-16h36.69L82.34,77.66A8,8,0,0,1,93.66,66.34L120,92.69V56a8,8,0,0,1,16,0V92.69l26.34-26.35a8,8,0,0,1,11.32,11.32L147.31,104H184a8,8,0,0,1,0,16Z"></path></svg>
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
