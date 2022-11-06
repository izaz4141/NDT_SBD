<template>
  <div
    class="fixed md:static bg-slate-200 dark:bg-main-dark-bg navbar w-full zindex"
  >
    <div class="grid grid-cols-3 relative md:mx-6 top-0">
      <div class="flex justify-start relative">
        <!-- this is the sidebar toggle -->
        <button
          @click="handleSidebarToggle"
          :style="{ color: currentColor }"
          class="relative text-xl rounded-full p-2 my-1 hover:bg-light-gray"
        >
          <Icon icon="ic:outline-menu" />
        </button>
      </div>
      <div class="flex justify-center items-center">
        <!-- search bar -->
        <SearchBar searchClass="w-72 h-6 pl-8 pr-2" inputClass="text-lg" />
      </div>
      <div class="flex justify-end gap-2">
        <!-- chat -->
        <button
          @click="handleChatClick"
          :style="{ color: currentColor }"
          class="relative text-xl rounded-full p-2 my-1 hover:bg-light-gray"
        >
          <Icon icon="ph:chat-teardrop-text" />
        </button>
        <!-- notif mdi:bell-ring-outline -->
        <button
          @click="handleNotificationClick"
          :style="{ color: currentColor }"
          class="relative text-xl rounded-full p-2 my-1 hover:bg-light-gray"
        >
          <Icon icon="mdi:bell-outline" />
        </button>
        <!-- profile -->
        <div
          class="flex items-center gap-2 cursor-pointer my-1 px-1 hover:bg-light-gray rounded-lg"
          @click="handleProfileClick"
        >
          <img :src="avatar" alt="user-profile" class="rounded-full w-8 h-8" />
          <p>
            <span class="dark:text-gray-400 text-14">Halo, </span>
            <span class="dark:text-gray-400 font-bold ml-1 text-14" v-if="user"
              >{{ user.name }}!</span
            >
            <span class="dark:text-gray-400 font-bold ml-1 text-14" v-else
              >Guest!</span
            >
          </p>
          <Icon icon="material-symbols:keyboard-arrow-down-rounded" />
        </div>
        <!-- conditional chat,notif,profile dropdown rendering -->
        <Chat v-if="chatOpen" />
        <Notification v-if="notificationOpen" />
        <ProfileDropdown v-if="profileOpen" />
      </div>
    </div>
  </div>
</template>

<script setup>
  import { Icon } from '@iconify/vue'
  import { ref, provide, inject } from 'vue'
  import avatar from '../assets/avatar_g1.jpg'
  import Chat from './Chat.vue'
  import Notification from './Notification.vue'
  import ProfileDropdown from './ProfileDropdown.vue'
  import SearchBar from './SearchBar.vue'

  const activeMenu = inject('activeMenu')
  const user = inject('user')
  const currentColor = inject('currentColor')

  const chatOpen = ref(false)
  const notificationOpen = ref(false)
  const profileOpen = ref(false)

  provide('chatOpen', chatOpen)
  provide('notificationOpen', notificationOpen)
  provide('profileOpen', profileOpen)

  const handleChatClick = () => {
    chatOpen.value = !chatOpen.value
  }
  const handleNotificationClick = () => {
    notificationOpen.value = !notificationOpen.value
  }
  const handleProfileClick = () => {
    profileOpen.value = !profileOpen.value
  }
  const handleSidebarToggle = () => {
    activeMenu.value = !activeMenu.value
  }
</script>

<style scoped>
  .zindex {
    z-index: 1000;
  }
</style>
