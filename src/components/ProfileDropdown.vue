<template>
  <div
    v-on-click-outside="handleProfileClose"
    class="zindex absolute right-1 top-16 bg-neutral-200 border-2 border-[#42464D] dark:bg-[#42464D] dark:border-zinc-900 pt-4 pb-4 pr-8 pl-8 rounded-lg w-96"
  >
    <div class="flex justify-between items-center">
      <p class="font-semibold text-lg dark:text-gray-200">Profil User</p>
      <button
        class="text-2xl p-2 hover:drop-shadow-xl hover:bg-light-gray"
        :style="{ borderRadius: '50%', color: 'rgb(153, 171, 180)' }"
        @click="handleProfileClose"
      >
        <Icon icon="ic:twotone-cancel" />
      </button>
    </div>
    <div class="flex gap-5 items-center mt-6 border-color border-b-1 pb-6">
      <img class="rounded-full h-24 w-24" :src="avatar" alt="user-profile" />
      <div>
        <p class="font-semibold text-lg dark:text-gray-200">
          {{ user ? user.name : 'Guest' }}
        </p>
        <p
          class="text-gray-500 text-sm dark:text-gray-400"
          :style="{ color: currentColor }"
        >
          {{ user ? user.author_level : 3 }}
        </p>
        <p class="text-gray-500 text-sm font-semibold dark:text-gray-400">
          Campers.co
        </p>
      </div>
    </div>
    <div>
      <div
        v-for="(item, index) in userProfileData"
        :key="index"
        @click="() => router.push(item.link)"
      >
        <div
          v-if="conditionalRow(item.title)"
          class="flex gap-5 border-b-1 border-color p-4 hover:bg-light-gray cursor-pointer dark:hover:bg-[#42464D]"
        >
          <button
            type="button"
            :style="{ color: item.iconColor, background: item.iconBg }"
            class="text-xl rounded-lg p-3 hover:bg-light-gray"
          >
            <Icon :icon="item.icon" />
          </button>
          <div>
            <p class="font-semibold dark:text-gray-200">{{ item.title }}</p>
            <p class="text-gray-500 text-sm dark:text-gray-400">
              {{ item.desc }}
            </p>
          </div>
        </div>
      </div>
    </div>
    <div class="mt-5">
      <button
        v-if="user"
        class="text-white w-full"
        :style="{ background: currentColor, borderRadius: '10px' }"
        @click="handleLogout"
      >
        Logout
      </button>
      <div v-else class="flex justify-around">
        <button
          class="text-white w-2/5"
          :style="{ background: currentColor, borderRadius: '10px' }"
          @click="handleLogin"
        >
          Login
        </button>
        <button
          class="text-white w-2/5"
          :style="{ background: currentColor, borderRadius: '10px' }"
          @click="handleRegister"
        >
          Register
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { Icon } from '@iconify/vue'
  import { ref, inject } from 'vue'
  import { vOnClickOutside } from '@vueuse/components'
  import avatar from '../assets/avatar_g1.jpg'
  import { userProfileData } from '../data/dummy'
  import { useRouter } from 'vue-router'
  import httpClient from '../api/api'

  const user = inject('user')
  const user_id = inject('user_id')
  const currentColor = inject('currentColor', ref('#03C9D7'))
  const profileOpen = inject('profileOpen', ref(false))

  const router = useRouter()

  const user_provider = async () => {
    try {
      const resp = await httpClient.post('/@me', {
        user_id: user_id.value,
      })
      user.value = resp.data
    } catch (error) {
      user.value = false
      console.log('Not Authorized')
    }
  }
  const conditionalRow = (title) => {
    if (title == 'My Tasks') {
      if (user.value) {
        if (user.value.author_level <= 1) {
          return true
        }
      } else {
        return false
      }
    } else {
      return true
    }
  }

  const handleProfileClose = () => {
    profileOpen.value = false
  }
  const handleLogout = async () => {
    try {
      user_id.value = ''
      await user_provider()
    } catch (er) {
      console.log(er)
    }
  }
  const handleLogin = () => {
    router.push('/login')
  }
  const handleRegister = () => {
    router.push('/register')
  }
</script>

<style lang="css" scoped>
  .zindex {
    z-index: 100;
  }
</style>
