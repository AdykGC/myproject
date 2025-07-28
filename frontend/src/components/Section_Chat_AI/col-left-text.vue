<template>
  <div class="col left">
    <p class="heading" style="font-size: 2.3rem; font-weight: 600; color: rgb(255 255 255)">
      <span>Hi there!</span>
    </p>
    <p class="heading" style="font-size: 2.7rem; font-weight: 900; color: rgb(255 255 255)">
      <span>What would you like to know?</span>
    </p>
    <p class="heading" style="font-size: 1.6rem; font-weight: 100; color: rgb(255 255 255 / 55%)">
      <span>Use one of the most common prompts below <br> or ask your own question</span>
    </p>
  </div>
</template>


<style scoped>
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
.heading {
  margin: 0;
  line-height: 1.2;
}
.heading + .heading {
  margin-top: 10px;
}
</style>