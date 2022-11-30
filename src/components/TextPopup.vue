<template>
  <div
    class="fixed bg-half-transparent z-[1000] rounded-lg"
    v-on-click-outside="HandleClose"
  >
    <div
      class="text-black dark:text-gray-200 bg-white dark:bg-[#484B52] rounded-lg p-2 border-2 border-slate-800"
    >
      <div class="flex mx-2 items-center justify-between">
        <h1 class="text-center text-lg font-extrabold mb-2">{{ title }}</h1>
        <button
          class="text-lg p-1 hover:drop-shadow-sm w-min h-min hover:bg-light-gray relative"
          @click="HandleClose"
          :style="{ color: 'rgb(153, 171, 180)', borderRadius: '50%' }"
        >
          <Icon icon="ic:twotone-cancel" />
        </button>
      </div>
      <p class="mt-2">{{ isi }}</p>
    </div>
  </div>
</template>

<script setup>
  import { inject } from 'vue'
  import { Icon } from '@iconify/vue'
  import { vOnClickOutside } from '@vueuse/components'

  const open = inject('popupOpen')

  const HandleClose = () => {
    open.value = false
  }

  const props = defineProps({
    title: {
      type: String,
    },
    isi: {
      type: String,
    },
  })
</script>

<style scoped></style>
