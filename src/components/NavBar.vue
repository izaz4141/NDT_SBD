<template>
  <div class="fixed md:static bg-slate-200 dark:bg-main-dark-bg w-full zindex">
    <div class="relative md:mx-6 top-0 flex justify-between" ref="wrapperEl">
      <div class="flex relative gap-5" v-if="!activeMenu">
        <!-- this is the sidebar toggle -->
        <button
          @click="handleSidebarToggle"
          :style="{ color: currentColor }"
          class="relative text-2xl rounded-full pl-2 my-auto hover:bg-light-gray"
        >
          <Icon icon="material-symbols:keyboard-double-arrow-right-rounded" />
        </button>
        <a
          class="items-center gap-3 flex text-xl font-extrabold tracking-tight mr-3 dark:text-white text-slate-900"
          href=""
        >
          <Icon icon="fa-solid:campground" />
          <span>Campers</span>
        </a>
      </div>
      <div
        class="flex justify-center items-center invisible w-0 md:visible md:w-auto"
        :class="{ 'ml-12': activeMenu }"
      >
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
          class="flex items-center md:gap-2 cursor-pointer my-1 px-1 py-0 md:p-1 hover:bg-light-gray rounded-full md:rounded-lg"
          @click="handleProfileClick"
        >
          <img :src="avatar" alt="user-profile" class="rounded-full w-8 h-8" />
          <p class="flex w-0 invisible md:w-auto md:visible">
            <span class="dark:text-gray-400 text-14">Halo, </span>
            <span class="dark:text-gray-400 font-bold ml-1 text-14">
              {{ user ? user.name : 'Guest' }}!
            </span>
          </p>
          <Icon
            icon="material-symbols:keyboard-arrow-down-rounded"
            class="w-0 invisible md:w-auto md:visible"
          />
        </div>
        <!-- conditional chat,notif,profile dropdown rendering -->
        <div ref="popupEl">
          <Chat v-if="chatOpen" />
          <Notification v-if="notificationOpen" />
          <ProfileDropdown v-if="profileOpen" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { Icon } from '@iconify/vue'
  import { ref, provide, inject } from 'vue'
  import { useAutoAnimate } from '@formkit/auto-animate/vue'

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
  const [wrapperEl] = useAutoAnimate()
  const [popupEl] = useAutoAnimate()
</script>

<style scoped>
  .zindex {
    z-index: 500;
  }
</style>
