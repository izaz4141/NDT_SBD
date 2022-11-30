<template>
  <div
    class="flex flex-col justify-center my-12 text-center md:text-sm text-xs"
  >
    <h1>Inventaris</h1>
    <SearchBar
      searchClass="w-[24rem] h-10 pl-8 pr-2 rounded-lg"
      v-model="searchFilter"
      inputClass="text-sm md:text-base"
      :submitFunc="querySearch"
      class="m-auto my-4"
      :style="{ borderColor: currentColor }"
    />
    <TabelPeminjaman />
  </div>
</template>

<script setup>
  import { ref, inject, onBeforeMount, watch, provide } from 'vue'
  import { useRouter } from 'vue-router'
  import httpClient from '../api/api'
  import SearchBar from '../components/SearchBar.vue'
  import TabelPeminjaman from '../components/TabelPeminjaman.vue'

  const router = useRouter()
  const data = ref([])
  const data_q = ref([])
  const searchFilter = ref('')

  const user = inject('user')
  const currentColor = inject('currentColor')

  provide('data_peminjaman', data_q)

  const filterByValue = (array, string) => {
    return array.filter((o) =>
      Object.keys(o).some(
        (k) =>
          typeof o[k] === 'string' &&
          o[k].toLowerCase().includes(string.toLowerCase()),
      ),
    )
  }
  const querySearch = () => {
    const data_out = filterByValue(data.value, searchFilter.value)
    data_q.value = data_out
  }

  const data_provider = async () => {
    if (user.value) {
      try {
        const resp = await httpClient.post('/peminjaman_list', {
          author_level: user.value.author_level,
        })
        data.value = resp.data
      } catch (er) {
        console.log(er)
      }
    } else {
      router.push('/')
    }
  }
  onBeforeMount(async () => {
    await data_provider()
    data_q.value = data.value
  })
  watch(
    data,
    () => {
      querySearch()
    },
    { deep: true },
  )
</script>

<style scoped></style>
