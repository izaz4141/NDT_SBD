<template>
  <div ref="wrapperEl" class="zindex">
    <div
      v-if="activeMenu"
      class="w-72 fixed sidebar dark:bg-secondary-dark-bg bg-slate-400 border-r-2 border-zinc-900 text-black dark:text-white scroller"
    >
      <div
        class="h-screen md:overflow-hidden overflow-auto md:hover:overflow-auto pb-10"
      >
        <div class="bg-slate-300 dark:bg-main-dark-bg">
          <div class="flex justify-between items-center navHeight">
            <a
              class="items-center gap-3 ml-3 flex text-xl font-extrabold tracking-tight dark:text-white text-slate-900"
              href=""
            >
              <Icon icon="fa-solid:campground" />
              <span>Campers</span>
            </a>
            <button
              class="text-2xl mr-3 block pr-2 my-2 hover:border-light-gray hover:border-1"
              @click="closeMenu"
              :style="{ color: currentColor }"
            >
              <Icon
                icon="material-symbols:keyboard-double-arrow-left-rounded"
              />
            </button>
          </div>
          <div class="h-6"></div>
        </div>
        <ChildBar :links="links" />
      </div>
    </div>
  </div>
</template>

<script setup>
  import ChildBar from './ChildBar.vue'
  import { links } from '../data/dummy'
  import { Icon } from '@iconify/vue'
  import { ref, inject, onMounted, watch } from 'vue'
  import { useAutoAnimate } from '@formkit/auto-animate/vue'

  const activeMenu = inject('activeMenu', ref(true))
  const screenSize = inject('screenSize', ref(window.innerWidth))
  const currentColor = inject('currentColor', ref('#03C9D7'))
  const [wrapperEl] = useAutoAnimate()

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
    if (screenSize.value <= 900) {
      activeMenu.value = false
    } else {
      activeMenu.value = true
    }
  })
</script>

<style scoped>
  .zindex {
    z-index: 1000;
  }
  .scroller {
    scrollbar-width: thin;
  }
  .scroller::-webkit-scrollbar {
    width: 2vw;
  }
  .navHeight {
    height: 46px;
  }
</style>
