<script setup language="js">
  // This starter template is using Vue 3 <script setup> SFCs
  // Check out https://vuejs.org/api/sfc-script-setup.html#script-setup
  // import HelloWorld from './components/HelloWorld.vue'
  import SideBar from './components/SideBar.vue'
  import { ref, provide, onMounted } from 'vue'
  import { useStorage, useDark, useStorageAsync } from '@vueuse/core'
  import { useAutoAnimate } from '@formkit/auto-animate/vue'

  import ThemePopup from './components/ThemePopup.vue'
  import SetCon from './components/SetCon.vue'
  import NavBar from './components/NavBar.vue'
  import Footer from './components/Footer.vue'

  const user = ref(useStorageAsync('user', false, localStorage))

  const activeMenu = ref(true)
  const themeOpen = ref(false)
  const screenSize = ref(window.innerWidth)
  const currentColor = ref(useStorage('colodMode', '#03C9D7', localStorage))
  const currentDark = ref(useStorage('themeMode', useDark(), localStorage))

  provide('user', user)
  provide('currentColor', currentColor)
  provide('activeMenu', activeMenu)
  provide('themeOpen', themeOpen)
  provide('screenSize', screenSize)
  provide('currentDark', currentDark)

  const user_provider = async () => {
    try {
      const resp = await httpClient.get('/@me')
      user.value = resp.data
    } catch (error) {
      console.log('Not Authorized')
    }
  }

  const [wrapperEl] = useAutoAnimate()
  const [contEl] = useAutoAnimate()

  onMounted(() => {
    user_provider()
    if (screenSize.value <= 900) {
      activeMenu.value = false
    }
  })
</script>

<template>
  <div class="flex relative dark:bg-main-dark-bg" ref="contEl">
    <SideBar v-if="activeMenu" />
    <SetCon />
    <div
      class="bg-main-bg min-h-screen w-full"
      :class="{ 'md:ml-72': activeMenu, '': !activeMenu }"
    >
      <NavBar />
      <div
        class="bg-white dark:bg-secondary-dark-bg overflow-auto dark:text-white min-h-screen"
      >
        <div class="mt-24 md:mt-0" ref="wrapperEl">
          <ThemePopup v-if="themeOpen" />
          <router-view />
        </div>
      </div>
      <Footer />
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
