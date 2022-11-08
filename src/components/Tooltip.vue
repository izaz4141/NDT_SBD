<template>
  <div
    class="absolute w-auto p-2 m-2 min-w-max rounded-md shadow-md text-xs font-bold transition-all duration-100 origin-left text-white bg-gray-900"
    :style="{ color: textColor, background: backgroundColor }"
  >
    {{ text }}
  </div>
</template>

<script setup>
  const props = defineProps({
    text: {
      type: String,
      default: 'Text Here',
    },
    textColor: {
      type: String,
      default: '',
    },
    backgroundColor: {
      type: String,
      default: '',
    },
  })
</script>

<style lang="css" scoped></style>
