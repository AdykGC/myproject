<template>
    <header>
        <nav>
            <router-link to="/">Home</router-link>
            <router-link to="/items">Items</router-link>
            <router-link to="/about">About</router-link>
        </nav>
    </header>
</template>

<script>
export default {
  name: "Header",
};
</script>

<style scoped>
header {
  background-color: #f5f5f5;
  padding: 1rem;
}

nav a {
  margin-right: 10px;
  text-decoration: none;
  color: #333;
}
</style>
