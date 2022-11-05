<template>
  <div class="bg-half-transparent w-screen fixed nav-item top-0 right-0">
    <div
      class="float-right h-screen text-black dark:text-gray-200 bg-white dark:bg-[#484B52] w-400"
    >
      <div class="flex justify-between items-center p-4 ml-4">
        <p class="font-semibold text-lg">Pengaturan</p>
        <button
          class="text-2xl p-3 hover:drop-shadow-xl hover:bg-light-gray"
          @click="HandleClose"
          :style="{ color: 'rgb(153, 171, 180)', borderRadius: '50%' }"
        >
          <Icon icon="ic:twotone-cancel" />
        </button>
      </div>
      <div class="flex-col border-t-1 border-color p-4 ml-4">
        <p class="font-semibold text-xl">Opsi Tema</p>
        <div class="mt-4">
          <button
            v-if="currentDark"
            class="bg-white border-2 border-black text-black py-2 px-4"
            @click="toggleMode('Light')"
          >
            Toggle to Light Mode
          </button>
          <button
            v-else
            class="bg-main-dark-bg border-2 border-white text-white py-2 px-4"
            @click="toggleMode('Dark')"
          >
            Toggle to Dark Mode
          </button>
        </div>
      </div>
      <div class="p-4 border-t-1 border-color ml-4">
        <p class="font-semibold text-xl">Warna Tema</p>
        <div class="flex gap-3">
          <div
            v-for="(item, index) in themeColors"
            class="relative mt-2 cursor-pointer flex gap-5 items-center"
            :key="index"
          >
            <button
              @click="setColor(item.color)"
              :style="{ backgroundColor: item.color }"
              class="h-10 w-10 rounded-full cursor-pointer"
            >
              <Icon
                icon="material-symbols:check-circle"
                class="ml-2 text-2xl text-white"
                :class="item.color === currentColor ? 'block' : 'hidden'"
              />
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { inject, ref } from 'vue'
  import { Icon } from '@iconify/vue'
  import { useToggle } from '@vueuse/core'
  import { themeColors } from '../data/dummy'

  const themeOpen = inject('themeOpen', ref(false))
  const currentColor = inject('currentColor')
  const currentDark = inject('currentDark')

  const HandleClose = () => {
    themeOpen.value = false
  }
  // const isDark = useDark()
  const toggleDark = useToggle(currentDark)
  const toggleMode = (mode) => {
    toggleDark()
    console.log(mode)
  }

  const setColor = (color) => {
    console.log(color)
    currentColor.value = color
  }
</script>

<style lang="scss" scoped></style>
