<template>
  <div
    class="flex flex-col justify-center my-12 text-center md:text-sm text-xs"
  >
    <h1>Daftar Peralatan</h1>
    <SearchBar
      searchClass="w-[24rem] h-10 pl-8 pr-2 rounded-lg"
      v-model="searchFilter"
      inputClass="text-sm md:text-base"
      :submitFunc="querySearch"
      class="m-auto my-4"
      :style="{ borderColor: currentColor }"
    />
    <div class="flex justify-around items-center">
      <div>
        <label htmlFor="name" class="mr-4 font-bold">Nama</label>
        <input
          type="name"
          class="px-4 py-1 bg-white dark:bg-gray-900 rounded-md border-1"
          :style="{ borderColor: currentColor }"
          v-model="name"
        />
      </div>
      <div>
        <label htmlFor="tipe" class="mr-4 font-bold">Tipe</label>
        <input
          type="text"
          v-model="tipe"
          class="px-4 py-1 bg-white dark:bg-gray-900 rounded-md border-1"
          :style="{ borderColor: currentColor }"
        />
      </div>
      <button
        @click="handleAdd"
        class="bg-gray-600 hover:bg-gray-500 text-white py-2 px-3"
      >
        Add
      </button>
    </div>
    <TabelDaftarAlat />
  </div>
</template>

<script setup>
  import { ref, inject, onBeforeMount, watch, provide } from 'vue'
  import { useRouter } from 'vue-router'
  import httpClient from '../api/api'
  import SearchBar from '../components/SearchBar.vue'
  import TabelDaftarAlat from '../components/TabelDaftarAlat.vue'

  const router = useRouter()
  const data = ref([])
  const data_q = ref([])
  const name = ref('')
  const tipe = ref('')
  const searchFilter = ref('')

  const user = inject('user')
  const currentColor = inject('currentColor')

  provide('data_alat', data_q)

  const handleAdd = async () => {
    try {
      await httpClient.post('/add_inventaris', {
        name: name.value,
        tipe: tipe.value,
      })
      await data_provider()
    } catch (er) {
      console.log(er)
    }
  }
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
        const resp = await httpClient.post('/inventaris_list', {
          author_level: user.value.author_level,
        })
        data.value = resp.data
        console.log(resp.data)
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
