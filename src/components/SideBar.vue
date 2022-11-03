<template>
  <div
    class="w-72 fixed sidebar dark:bg-secondary-dark-bg bg-slate-200 border-r-2 border-zinc-900 text-black dark:text-white scroller"
  >
    <div
      class="h-screen md:overflow-hidden overflow-auto md:hover:overflow-auto pb-10"
    >
      <div class="ml-3 flex justify-between items-center">
        <a
          class="items-center gap-3 ml-3 mt-4 flex text-xl font-extrabold tracking-tight dark:text-white text-slate-900"
          href=""
        >
          <Icon icon="fa-solid:campground" />
          <span>Campers</span>
        </a>
        <button
          class="text-xl rounded-full p-3 hover:bg-light-gray mt-4 block"
          @click="closeMenu"
          :style="{ color: currentColor }"
        >
          <Icon icon="material-symbols:keyboard-double-arrow-left-rounded" />
        </button>
      </div>
      <ChildBar :links="links" />
    </div>
  </div>
</template>

<script setup>
  import ChildBar from './ChildBar.vue'
  import { links } from '../data/dummy'
  import { Icon } from '@iconify/vue'
  import { ref, inject, onMounted, watch } from 'vue'

  const activeMenu = inject('activeMenu', ref(true))
  const screenSize = inject('screenSize', ref(window.innerWidth))
  const currentColor = inject('currentColor', ref('#03C9D7'))

  const closeMenu = () => {
    activeMenu.value = !activeMenu.value
  }

  onMounted(() => {
    const handleResize = () => (screenSize.value = window.innerWidth)
    window.addEventListener('resize', handleResize)
    handleResize()

    return () => window.removeEventListener('resize', handleResize)
  })
  watch(screenSize, () => {
    if (screenSize <= 900) {
      activeMenu.value = false
    } else {
      activeMenu.value = true
    }
  })
</script>

<style scoped>
  .scroller {
    scrollbar-width: thin;
  }
  .scroller::-webkit-scrollbar {
    width: 2vw;
  }
</style>
