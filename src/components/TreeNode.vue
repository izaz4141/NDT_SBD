<template>
  <div
    class="bg-slate-300 dark:bg-slate-800 pb-4 rounded-xl items-center"
    ref="wrapperEl"
  >
    <div
      class="flex text-gray-300 dark:text-gray-500 uppercase items-center justify-between bg-slate-500 dark:bg-slate-900 hover:outline-1 hover:outline-white hover:outline hover:text-white pl-5 py-3 pr-2 rounded-xl"
      @click="HandleClick"
    >
      <p>{{ node.title }}</p>
    </div>
    <div
      class="ml-2"
      v-if="childVisible && node && node.children"
      v-for="link in node.children"
    >
      <router-link
        :to="link.url"
        class="flex items-center gap-5 pl-4 pt-3 pb-2.5 rounded-lg text-md dark:text-gray-200 dark:hover:text-black hover:bg-light-gray"
      >
        <Icon :icon="link.icon" />
        <span class="capitalize">{{ link.name }}</span>
      </router-link>
    </div>
  </div>
</template>

<script setup>
  import { ref, inject } from 'vue'
  import { Icon } from '@iconify/vue'
  import { useAutoAnimate } from '@formkit/auto-animate/vue'

  const childVisible = ref(false)
  const currentColor = inject('currentColor')

  const [wrapperEl] = useAutoAnimate()
  const HandleClick = () => {
    childVisible.value = !childVisible.value
  }

  const props = defineProps({
    node: {
      type: Object,
      default: null,
    },
  })
</script>

<style scoped>
  .router-link-active {
    color: white;
    background-color: v-bind('currentColor');
  }
  .router-link-active:hover {
    color: white;
  }
</style>
