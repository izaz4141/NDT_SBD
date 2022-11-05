<template>
  <div v-if="links" v-for="item in links">
    <div :key="item.title">
      <TreeNode :node="item" />
    </div>
  </div>
</template>

<script setup>
  import TreeNode from './TreeNode.vue'
  const props = defineProps({
    links: {
      type: Array,
      default: null,
    },
  })
</script>

<style lang="scss" scoped></style>
