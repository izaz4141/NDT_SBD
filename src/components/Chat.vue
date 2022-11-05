<template>
  <div
    v-on-click-outside="handleChatClose"
    class="nav-item absolute right-5 md:right-52 top-16 bg-neutral-200 border-2 border-[#42464D] dark:bg-[#42464D] dark:border-zinc-900 pt-4 pb-4 pr-8 pl-8 rounded-lg w-96"
  >
    <div class="flex justify-between items-center">
      <div class="flex gap-3">
        <p class="font-semibold text-lg dark:text-gray-200">Pesan</p>
        <button
          type="button"
          class="dark:text-white text-xs rounded p-1 px-2 bg-orange"
          :style="{ color: currentColor }"
        >
          2 New
        </button>
      </div>
      <button
        class="text-2xl p-2 hover:drop-shadow-xl hover:bg-light-gray"
        @click="handleChatClose"
        :style="{ color: 'rgb(153, 171, 180)', borderRadius: '50%' }"
      >
        <Icon icon="ic:twotone-cancel" />
      </button>
    </div>
    <div class="mt-5">
      <div
        class="flex items-center gap-5 border-b-1 border-color p-3 leading-8 cursor-pointer"
        v-for="(item, index) in chatData"
        :key="index"
      >
        <div class="relative">
          <img
            class="rounded-full h-10 w-10"
            :src="item.image"
            :alt="item.message"
          />
          <span
            class="absolute inline-flex rounded-full h-2 w-2 right-0 -top-1"
            :style="{ background: '#03C9D7' }"
          />
        </div>
        <div>
          <p class="font-semibold dark:text-gray-200">{{ item.message }}</p>
          <p class="text-gray-500 dark:text-gray-400 text-sm">
            {{ item.desc }}
          </p>
          <p class="text-gray-500 dark:text-gray-400 text-xs">
            {{ item.time }}
          </p>
        </div>
      </div>
      <div class="mt-5">
        <button
          class="text-white w-full"
          :style="{ background: currentColor, borderRadius: '10px' }"
        >
          Lihat Semua Pesan
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { Icon } from '@iconify/vue'
  import { ref, inject } from 'vue'
  import { chatData } from '../data/dummy'
  import { vOnClickOutside } from '@vueuse/components'

  const currentColor = inject('currentColor', ref('#03C9D7'))
  const chatOpen = inject('chatOpen', ref(false))

  const handleChatClose = () => {
    chatOpen.value = false
  }
</script>

<style scoped></style>
