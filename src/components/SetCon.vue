<template>
  <div class="fixed right-4 bottom-4" :style="{ zindex: '1000' }">
    <button
      @click="HandleClick"
      class="text-3x1 p-3 hover:drop-shadow-xl hover:bg-light-gray text-white"
      :style="{ color: currentColor, borderRadius: '50%' }"
    >
      <Icon icon="heroicons-outline:cog" />
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

<style lang="" scoped></style>
