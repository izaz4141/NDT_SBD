<script setup language="js">
  // This starter template is using Vue 3 <script setup> SFCs
  // Check out https://vuejs.org/api/sfc-script-setup.html#script-setup
  // import HelloWorld from './components/HelloWorld.vue'
  import SideBar from './components/SideBar.vue'
  import { ref, provide } from 'vue'
  import { useDark } from '@vueuse/core'
  import ThemePopup from './components/ThemePopup.vue'
  import SetCon from './components/SetCon.vue'

  const currentColor = ref('#03C9D7')
  const activeMenu = ref(true)
  const themeOpen = ref(false)
  const screenSize = ref(window.innerWidth)
  const currentDark = ref(useDark())

  provide('currentColor', currentColor)
  provide('activeMenu', activeMenu)
  provide('themeOpen', themeOpen)
  provide('screenSize', screenSize)
  provide('currentDark', currentDark)
</script>

<template>
  <div class="flex relative dark:bg-main-dark-bg">
    <SideBar />
    <SetCon />
    <div
      class="dark:bg-main-bg bg-main-bg min-h-screen w-full"
      :class="{ 'md:ml-72': activeMenu, 'flex-2': !activeMenu }"
    >
      <!-- navbar -->
      <div>
        <ThemePopup v-if="themeOpen" />
        <router-view />
      </div>
      <!-- footer -->
    </div>
  </div>
  <!-- <div>
    <a href="https://vitejs.dev" target="_blank">
      <img src="/vite.svg" class="logo" alt="Vite logo" />
    </a>
    <a href="https://vuejs.org/" target="_blank">
      <img src="./assets/vue.svg" class="logo vue" alt="Vue logo" />
    </a>
  </div>
  <HelloWorld msg="Vite + Vue" /> -->
</template>

<style scoped>
  .logo {
    height: 6em;
    padding: 1.5em;
    will-change: filter;
  }
  .logo:hover {
    filter: drop-shadow(0 0 2em #646cffaa);
  }
  .logo.vue:hover {
    filter: drop-shadow(0 0 2em #42b883aa);
  }
  html.dark {
    color-scheme: dark;
  }
</style>
