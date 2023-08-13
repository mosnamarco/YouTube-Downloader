<script setup>
import Welcome from './components/Welcome.vue';
import Download from './components/Download.vue';
</script>

<template>
  <div class="container">
    <main>
      <Welcome />
    </main>

    <Download />
  </div>
</template>

<style scoped>
.container {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 20rem;
}
</style>