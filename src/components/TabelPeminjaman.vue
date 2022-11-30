<template>
  <div class="my-6">
    <table class="flex flex-col justify-center w-[90%] m-auto">
      <thead class="w-full">
        <tr class="flex justify-around">
          <th class="w-[10%]" scope="col">Id</th>
          <th class="w-[15%]" scope="col">Nama Alat</th>
          <th class="w-[15%]" scope="col">Peminjam</th>
          <th class="w-[15%]" scope="col">Tanggal Pengambilan</th>
          <th class="w-[15%]" scope="col">Tanggal Pengembalian</th>
          <th class="w-[20%]" scope="col">Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="item in data"
          :key="item.id"
          class="border-b border-gray-700 flex justify-around w-full items-center"
        >
          <th
            scope="row"
            class="w-[10%] overflow-auto flex items-center justify-center"
          >
            <button
              @click="handleCopy(item.id)"
              class="bg-sky-500 hover:bg-sky-400 text-white font-bold py-1 px-2 rounded-t"
            >
              Copy
            </button>
          </th>
          <!-- Nama Alat -->
          <td class="w-[15%] overflow-auto">
            <div>
              {{ item.item.name }}
            </div>
          </td>
          <!-- Peminjam -->
          <td class="w-[15%] overflow-auto">
            <div>
              {{ item.peminjam.name }}
            </div>
          </td>
          <!-- Tanggal Pengambilan -->
          <td class="w-[15%] overflow-auto">
            <div>
              {{ item.tanggal_pengambilan }}
            </div>
          </td>
          <!-- Tanggal Pengembalian -->
          <td class="w-[15%] overflow-auto">
            <div>
              {{ item.tanggal_pengembalian }}
            </div>
          </td>
          <td class="w-[20%]">
            <div class="flex gap-2 justify-center items-center">
              <button
                v-if="item.tanggal_pengembalian"
                disabled
                class="bg-blue-500 hover:bg-blue-400 text-white font-bold py-1 px-4 rounded-t cursor-not-allowed brightness-50"
              >
                Sudah Kembali
              </button>
              <button
                v-else
                @click="handleKembali(item.id, item.item.id)"
                class="bg-blue-500 hover:bg-blue-400 text-white font-bold py-1 px-4 rounded-t"
              >
                Kembalikan
              </button>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
  import { inject } from 'vue'
  import httpClient from '../api/api'

  const user = inject('user')
  const data = inject('data_peminjaman')

  const handleKembali = async (id, i_id) => {
    try {
      await httpClient.post('/pengembalian', {
        peminjaman_id: id,
        item_id: i_id,
      })
      await data_provider()
    } catch (er) {
      console.log(er)
    }
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
  const handleCopy = (id) => {
    navigator.clipboard.writeText(id)
  }
</script>

<style scoped></style>
