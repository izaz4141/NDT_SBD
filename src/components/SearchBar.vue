<template>
  <div
    class="flex relative bg-white dark:bg-gray-900 rounded-md items-center focus-within:outline focus-within:outline-blue-600 focus-within:outline-2"
    :class="searchClass"
  >
    <button
      class="absolute inset-y-0 left-0 flex items-center pl-2 bg-transparent"
      :style="{ color: currentColor }"
    >
      <Icon icon="ion:ios-search" />
    </button>
    <input
      type="text"
      :placeholder="placeHolder"
      class="text-sm rounded-md w-full focus:outline-none focus:shadow-outline dark:text-white text-gray-900 bg-transparent"
      :class="inputClass"
    />
  </div>
</template>

<script setup>
  import { inject } from 'vue'
  import { Icon } from '@iconify/vue'
  const currentColor = inject('currentColor')

  const props = defineProps({
    searchClass: {
      type: String,
      default: '',
    },
    inputClass: {
      type: String,
      default: '',
    },
    placeHolder: {
      type: String,
      default: 'Search..',
    },
  })
</script>

<style lang="scss" scoped></style>
