<template>
    <div class="nav-right">
        <!-- Profile -->
        <router-link to="/profile" class="icon-link">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" viewBox="0 0 16 16">
                <path d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H3zm5-6a3 3 0 100-6 3 3 0 000 6z"/>
            </svg>
            <span>Profile</span>
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
