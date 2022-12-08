<template>
  <div v-if="links" v-for="item in links">
    <div :key="item.title" v-if="isPrivileged(item.title)">
      <TreeNode :node="item" />
    </div>
  </div>
</template>

<script setup>
  import TreeNode from './TreeNode.vue'
  import { inject } from 'vue'

  const user = inject('user')
  const isPrivileged = (title) => {
    if (forbiddenPelanggan.includes(title)) {
      if (user.value.author_level <= 1) {
        return true
      } else {
        return false
      }
    } else {
      return true
    }
  }
  const forbiddenPelanggan = ['DevTools', 'Employee']

  const props = defineProps({
    links: {
      type: Array,
      default: null,
    },
  })
</script>

<style lang="scss" scoped></style>
