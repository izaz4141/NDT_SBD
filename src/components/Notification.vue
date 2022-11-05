<template>
  <div
    v-on-click-outside="handleNotificationClose"
    class="nav-item absolute right-5 md:right-40 top-16 bg-neutral-200 border-2 border-[#42464D] dark:bg-[#42464D] dark:border-zinc-900 pt-4 pb-4 pr-8 pl-8 rounded-lg w-96"
  >
    <div class="flex justify-between items-center">
      <div class="flex gap-3">
        <p class="font-semibold text-lg dark:text-gray-200">Notifikasi</p>
        <button
          type="button"
          class="text-white text-xs rounded p-1 px-2 bg-orange-theme"
          :style="{
            color: currentColor,
          }"
        >
          2 Baru
        </button>
      </div>
      <button
        @click="handleNotificationClose"
        class="text-2xl p-2 hover:drop-shadow-xl hover:bg-light-gray"
        :style="{ color: 'rgb(153, 171, 180)', borderRadius: '50%' }"
      >
        <Icon icon="ic:twotone-cancel" />
      </button>
    </div>
    <div class="mt-5">
      <div
        class="flex items-center leading-8 gap-5 border-b-1 border-color p-3"
        v-for="(item, index) in chatData"
        :key="index"
      >
        <img
          class="rounded-full h-10 w-10"
          :src="item.image"
          :alt="item.message"
        />
        <div>
          <p class="font-semibold dark:text-gray-200">{{ item.message }}</p>
          <p class="text-gray-500 text-sm dark:text-gray-400">
            {{ item.desc }}
          </p>
        </div>
      </div>
      <div name="mt-5">
        <button
          @click="handleNotificationClose"
          class="text-white w-full"
          :style="{ background: currentColor, borderRadius: '10px' }"
        >
          Lihat Semua Notifikasi
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

  const notificationOpen = inject('notificationOpen', ref(false))
  const currentColor = inject('currentColor')

  const handleNotificationClose = () => {
    notificationOpen.value = false
  }
</script>

<style lang="css" scoped></style>
