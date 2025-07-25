<template>
  <header>
    <nav aria-label="Global navigation">
      <div class="utility-wrapper">
        <a href="https://www.wbgames.com" target="_blank" class="logo">
          <!-- Минималистичный SVG лого -->
          <svg viewBox="0 0 65 82" width="40" height="50" aria-hidden="true" focusable="false">
            <path d="M48.14,34.76c-1.79,0-3.41.68-8.42,4.25V58.23C48.39,48.54,50.86,41.9,50.86,38.5,50.86,36.12,49.75,34.76,48.14,34.76Z" fill="currentColor"/>
            <!-- Добавь другие пути по необходимости -->
          </svg>
        </a>

        <button @click="openLanguageModal" class="language-btn">
          🌐 United States - English
        </button>

        <a href="https://wbshop.com/collections/mortal-kombat" target="_blank" class="nav-item">
          SHOP MERCH
        </a>
      </div>

      <div class="links-wrapper">
        <a href="http://www.mortalkombat.com/en-us/pc-specs" class="nav-item">PC SPECS</a>
        <a href="https://mortalkombat1.bugs.wbgames.com/" target="_blank" class="nav-item">REPORT A BUG</a>
        <a href="https://mortalkombatgamessupport.wbgames.com/hc/categories/16745181128723" target="_blank" class="nav-item">Support</a>
        <a href="https://drive.google.com/file/d/1H5mzLqwYpyhhnsBvUVteQy8srn-wgz8R/view?usp=sharing" target="_blank" class="nav-item">KOMMUNITY KIT</a>
        <a href="http://www.mortalkombat.com/en-us/patch-notes" class="nav-item">PATCH NOTES</a>

        <div class="social-wrapper">
          <a href="https://www.youtube.com/@mortalkombat" target="_blank" aria-label="YouTube" class="social-btn">YT</a>
          <a href="https://www.facebook.com/mortalkombat" target="_blank" aria-label="Facebook" class="social-btn">FB</a>
          <!-- Добавь остальные соцсети, если нужно -->
        </div>
      </div>
    </nav>
  </header>
</template>

<script setup>
function openLanguageModal() {
  // здесь можно реализовать логику открытия модального окна выбора языка
  alert("Open language modal");
}
</script>

<style scoped>
header {
  width: 100%;
  background-color: #111;
  color: white;
  padding: 1rem;
  box-sizing: border-box;
}
.utility-wrapper, .links-wrapper {
  display: flex;
  align-items: center;
  gap: 1rem;
}
.logo svg {
  fill: currentColor;
}
.nav-item {
  color: white;
  text-decoration: none;
  font-weight: 600;
}
.language-btn {
  background: none;
  border: none;
  color: white;
  cursor: pointer;
  font-weight: 600;
}
.social-wrapper a {
  margin-left: 0.5rem;
  color: white;
  text-decoration: none;
  font-weight: 600;
}
</style>