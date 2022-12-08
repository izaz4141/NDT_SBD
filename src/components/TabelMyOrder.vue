<template>
  <div class="my-6">
    <table class="flex flex-col justify-center m-auto overflow-auto">
      <thead>
        <tr class="flex justify-around">
          <th class="w-[10vw]" scope="col">Id</th>
          <th class="w-[20vw]" scope="col">Lokasi</th>
          <th class="w-[10vw]" scope="col">Layanan</th>
          <th class="w-[10vw]" scope="col">Harga</th>
          <th class="w-[20vw]" scope="col">Petugas</th>
          <th class="w-[10vw]" scope="col">Deskripsi</th>
          <th class="w-[15vw]" scope="col">Tanggal Pemesanan</th>
          <th class="w-[15vw]" scope="col">Estimasi Pengerjaan</th>
          <th class="w-[15vw]" scope="col">Tanggal Penyelesaian</th>
          <th class="w-[20vw]" scope="col">Actions</th>
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
            class="w-[10vw] overflow-auto flex items-center justify-center"
          >
            <button
              @click="handleCopy(item.id)"
              class="bg-sky-500 hover:bg-sky-400 text-white font-bold py-1 px-2 rounded-t"
            >
              Copy
            </button>
          </th>
          <!-- Lokasi -->
          <td class="w-[20vw] overflow-auto">
            {{ item.lokasi }}
          </td>
          <!-- Layanan -->
          <td class="w-[10vw] overflow-auto">
            {{ item.layanan }}
          </td>
          <!-- Harga -->
          <td class="w-[10vw] overflow-auto">
            <div>
              {{ item.harga }}
            </div>
          </td>
          <!-- Petugas -->
          <td class="w-[20vw] overflow-auto">
            <div>
              {{ item.karyawan.map((k) => k.name).join(', ') }}
            </div>
          </td>
          <!-- Deskripsi -->
          <td class="w-[10vw] justify-center flex items-center overflow-auto">
            <button
              @click="handleDeskripsi(item.id)"
              class="bg-violet-500 hover:bg-violet-400 text-white font-bold py-1 px-2 rounded-t"
            >
              Deskripsi
            </button>
          </td>
          <!-- Tanggal Pemensanan -->
          <td class="w-[15vw] overflow-auto">
            {{ item.tanggal_pemesanan }}
          </td>
          <!-- Estimasi Pengerjaan -->
          <td class="w-[15vw] overflow-auto">
            {{ item.estimasi_pengerjaan }}
          </td>
          <!-- Tanggal Penyelesaian -->
          <td class="w-[15vw] overflow-auto">
            {{ item.tanggal_selesai }}
          </td>
          <td class="w-[20vw]">
            <div class="flex gap-2 justify-center items-center">
              <button
                @click="handleDelete(item.id)"
                class="bg-red-500 hover:bg-red-400 text-white font-bold py-1 px-4 rounded-t"
              >
                Cancel Order
              </button>
            </div>
          </td>
          <TextPopup
            v-if="descOpen[item.id]"
            title="Deskripsi"
            :isi="item.deskripsi"
          />
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
  import { inject, onMounted, ref, provide } from 'vue'
  import httpClient from '../api/api'
  import TextPopup from './TextPopup.vue'
  import { useRouter } from 'vue-router'

  const router = useRouter()

  const user = inject('user')
  const data = inject('data_myOrder')

  const karyawan = ref([])
  const descOpen = ref({})

  provide('popupOpen', descOpen)

  const get_karyawan = async () => {
    try {
      const resp = await httpClient.get('/get_karyawan')
      karyawan.value = resp.data
    } catch (er) {
      console.log(er)
    }
  }

  const handleDelete = async (id) => {
    try {
      await httpClient.post('/cancel_order', {
        order_id: id,
      })
      await data_provider()
    } catch (er) {
      console.log(er)
    }
  }
  const handleDeskripsi = (id) => {
    descOpen.value = {}
    descOpen.value[id] = true
  }
  const data_provider = async () => {
    if (user.value) {
      try {
        const resp = await httpClient.post('/your_order_list', {
          user_id: user.value.id,
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
  onMounted(() => {
    get_karyawan()
  })
</script>

<style scoped></style>
