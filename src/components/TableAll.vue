<template>
  <table>
    <tbody>
      <tr>
        <th v-for="nama in Object.keys(data[0])" :key="nama">
          {{ nama }}
        </th>
      </tr>
      <tr v-for="item in data" :key="item.id">
        <td v-for="nama in item" :key="nama">
          {{ nama }}
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script setup>
  const props = defineProps({
    data: {
      type: Array,
      default: null,
    },
  })
</script>
