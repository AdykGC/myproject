<template>
  <section class="cta-section">
    <div class="container">
      <div class="cta-box">
        <div class="row">
          <div class="col left">
            <h2 class="heading">
              <span>Hi there!</span>
            </h2>

            <h1 class="heading">
              <span>What would you like to know?</span>
            </h1>

            <h4 class="heading">
              <span>Use one of the most commun prompts below or ask your own question</span>
            </h4>
          </div>
          <div class="col right">
            <a href="#" class="btn btn-light">Get Pro Version</a>
            <a href="#" class="btn btn-dark">Start Free Trial</a>
          </div>
        </div>
        <!-- Background SVGs -->
        <span class="bg-svg top-left">
          <!-- SVG code... -->
        </span>
        <span class="bg-svg bottom-right">
          <!-- SVG code... -->
        </span>
      </div>
    </div>
    <v-btn>Button</v-btn>
  </section>
</template>

<style scoped>
.cta-section {
  width: 100vw;
  position: relative;
  left: 50%;
  right: 50%;
  margin-left: -50vw;
  margin-right: -50vw;
  padding: 80px 0;
  background-color: #ffffff;
}
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 16px;
}
.cta-box {
  position: relative;
  background-color: #04004b; /* bg-primary */
  border-radius: 8px;
  padding: 70px;
  overflow: hidden;
  z-index: 1;
}
.row {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 20px;
}
.col {
  flex: 1 1 50%;
  padding: 16px;
}
.left {
  display: flex;
  flex-direction: column; /* расположить элементы вертикально */
  justify-content: flex-start;
  align-items: flex-start; /* выравнивание по левому краю */
  gap: 16px; /* расстояние между заголовками */
}

.right {
  display: flex;
  justify-content: flex-end;
  gap: 16px;
  flex-wrap: wrap;
}
.subheading {
  display: block;
  margin-bottom: 16px;
  font-size: 16px;
  font-weight: 500;
  color: white;
}
.heading {
  margin: 0;
  font-weight: bold;
  color: white;
  line-height: 1.2;
}
.heading + .heading {
  margin-top: 10px;
}
.btn {
  padding: 12px 28px;
  font-size: 16px;
  font-weight: 500;
  border-radius: 6px;
  text-decoration: none;
  transition: all 0.3s ease;
}
.btn-light {
  background-color: #ffffff;
  color: #4f46e5;
}
.btn-light:hover {
  background-color: #f3f4f6;
}
.btn-dark {
  background-color: #ec4899;
  color: white;
}
.btn-dark:hover {
  opacity: 0.9;
}
.bg-svg {
  position: absolute;
  z-index: -1;
}
.top-left {
  top: 0;
  left: 0;
}
.bottom-right {
  bottom: 0;
  right: 0;
}
</style>
