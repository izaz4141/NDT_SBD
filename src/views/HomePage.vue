<template>
  <div class="text-center">
    <div>This is HomePage</div>
    <div>{{ screenSize }}</div>
  </div>
</template>

<script setup>
  import { inject } from 'vue'
  const screenSize = inject('screenSize')
</script>

<style lang="" scoped></style>
