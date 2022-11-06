<template>
  <div class="fixed right-4 bottom-4 zindex">
    <button
      @click="HandleClick"
      class="p-2 hover:drop-shadow-xl hover:bg-light-gray bg-slate-300 dark:bg-main-dark-bg dark:hover:bg-secondary-dark-bg"
      :style="{ color: currentColor, borderRadius: '50%' }"
    >
      <Icon icon="heroicons-outline:cog" class="text-2xl" />
    </button>
  </div>
</template>

<script setup>
  import { ref, inject } from 'vue'
  import { Icon } from '@iconify/vue'

  const themeOpen = inject('themeOpen', ref(false))
  const currentColor = inject('currentColor', ref('#1A97F5'))
  const HandleClick = () => {
    themeOpen.value = !themeOpen.value
  }
</script>

<style lang="css" scoped>
  .zindex {
    z-index: 1000;
  }
</style>
