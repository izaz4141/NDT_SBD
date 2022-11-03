<template>
  <div class="bg-slate-800 pb-4 rounded-xl items-center">
    <div
      class="flex text-gray-400 uppercase items-center justify-between bg-slate-900 hover:outline-1 hover:outline-white hover:outline hover:text-white pl-5 py-3 pr-2 rounded-xl"
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
        class="dark:text-gray-200 dark:hover:text-black hover:bg-light-gray flex items-center gap-5 pl-4 pt-3 pb-2.5 rounded-lg text-md"
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
  const childVisible = ref(false)
  const currentColor = inject('currentColor', ref('#03C9D7'))
  const HandleClick = () => {
    childVisible.value = !childVisible.value
  }
  const props = defineProps({
    node: {
      type: Object,
      default: null,
    },
  })
  console.log(this)
</script>

<style lang="" scoped></style>
