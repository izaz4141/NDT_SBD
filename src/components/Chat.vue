<template>
  <div
    v-on-click-outside="handleChatClose"
    class="zindex absolute right-5 md:right-52 top-16 bg-neutral-200 border-2 border-[#42464D] dark:bg-[#42464D] dark:border-zinc-900 pt-4 pb-4 pr-8 pl-8 rounded-lg w-96"
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
    <div
      class="mt-5 overflow-y-auto min-h-[10vh] flex flex-col w-full max-h-[50vh]"
      id="chat_container"
    >
      <div
        class="flex items-center gap-5 border-b-1 border-color p-3 leading-8 cursor-pointer"
        v-for="(item, index) in chatLog"
        :key="index"
      >
        <div class="relative">
          <img
            class="rounded-full h-10 w-10"
            :src="avatar_g1"
            :alt="item.message"
          />
          <!-- <span
            class="absolute inline-flex rounded-full h-2 w-2 right-0 -top-1"
            :style="{ background: '#03C9D7' }"
          /> -->
        </div>
        <div>
          <p class="font-semibold dark:text-gray-200">{{ item.nama }}</p>
          <p class="text-gray-500 dark:text-gray-400 text-xs">
            {{ item.message }}
          </p>
        </div>
      </div>
      <div ref="bottom" />
    </div>
    <form
      class="mt-5 items-end flex justify-around"
      @submit.prevent="handleSend"
    >
      <input type="name" class="w-[80%] rounded-md" id="" v-model="chatInput" />
      <button
        class="text-white rounded-full p-1"
        :style="{ background: currentColor, borderRadius: '10px' }"
      >
        <Icon icon="ic:baseline-send" />
      </button>
    </form>
  </div>
</template>

<script setup>
  import { Icon } from '@iconify/vue'
  import { ref, inject, onMounted, nextTick, watch } from 'vue'
  import { useStorage } from '@vueuse/core'
  import { chatData } from '../data/dummy'
  import { vOnClickOutside } from '@vueuse/components'
  import avatar_g1 from '../assets/avatar_g1.jpg'

  const currentColor = inject('currentColor', ref('#03C9D7'))
  const chatOpen = inject('chatOpen', ref(false))
  const user = inject('user')
  const chatLog = ref(useStorage('chatLog', [], localStorage))
  const chatInput = ref('')
  const bottom = ref(null)

  const handleSend = () => {
    if (chatInput.value === '') {
      return
    }
    const nama = user.value ? user.value.name : 'Guest'
    chatLog.value.push({
      nama: nama,
      message: chatInput.value,
    })
    chatInput.value = ''
  }

  const handleChatClose = () => {
    chatOpen.value = false
  }

  onMounted(() => {
    bottom.value?.scrollIntoView({
      behavior: 'smooth',
      block: 'nearest',
      inline: 'start',
    })
  })
  watch(
    chatLog,
    () => {
      nextTick(() => {
        bottom.value?.scrollIntoView({
          behavior: 'smooth',
          block: 'nearest',
          inline: 'start',
        })
      })
    },
    {
      deep: true,
    },
  )
</script>

<style scoped>
  .zindex {
    z-index: 100;
  }
</style>
