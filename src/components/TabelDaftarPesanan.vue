<template>
  <div class="my-6">
    <table class="flex flex-col justify-center m-auto overflow-auto">
      <thead>
        <tr class="flex justify-around">
          <th class="w-[10vw]" scope="col">Id</th>
          <th class="w-[20vw]" scope="col">Lokasi</th>
          <th class="w-[10vw]" scope="col">Layanan</th>
          <th class="w-[10vw]" scope="col">Harga</th>
          <th class="w-[10vw]" scope="col">Pemesan</th>
          <th class="w-[20vw]" scope="col">Petugas</th>
          <th class="w-[10vw]" scope="col">Deskripsi</th>
          <th class="w-[15vw]" scope="col">Tanggal Pemesanan</th>
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
            <div v-if="editOpen[item.id]">
              <input
                type="text"
                v-model="editPrice"
                class="px-4 py-1 bg-white dark:bg-gray-900 rounded-md border-1"
                :style="{ borderColor: currentColor }"
              />
            </div>
            <div v-else>
              {{ item.harga }}
            </div>
          </td>
          <!-- Pemesan -->
          <td class="w-[10vw] overflow-auto">
            {{ item.pelanggan.name }}
          </td>
          <!-- Petugas -->
          <td class="w-[20vw] overflow-auto">
            <div v-if="editOpen[item.id]">
              <select
                class="px-4 py-1 bg-white dark:bg-gray-900 rounded-md border-1"
                v-model="editPetugas"
              >
                <option v-for="petugas in karyawan" :value="petugas.id">
                  {{ petugas.name }}
                </option>
              </select>
            </div>
            <div v-else>
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
          <!-- Tanggal Penyelesaian -->
          <td class="w-[15vw] overflow-auto">
            {{ item.tanggal_selesai }}
          </td>
          <td class="w-[20vw]">
            <div class="flex gap-2 justify-center items-center">
              <button
                v-if="editOpen[item.id]"
                @click="handleSave(item.id)"
                class="bg-green-500 hover:bg-green-400 text-white font-bold py-1 px-4 rounded-t"
              >
                Save
              </button>
              <button
                v-else
                @click="handleEdit(item)"
                class="bg-blue-500 hover:bg-blue-400 text-white font-bold py-1 px-4 rounded-t"
              >
                Edit
              </button>

              <button
                @click="handleDelete(item.id)"
                class="bg-red-500 hover:bg-red-400 text-white font-bold py-1 px-4 rounded-t"
              >
                Delete
              </button>
              <button
                v-if="editOpen[item.id]"
                @click="handleEditClose"
                class="text-3xl rounded-full h-min w-min relative right-2"
              >
                <Icon icon="ic:twotone-cancel" />
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
  import { Icon } from '@iconify/vue'
  import TextPopup from './TextPopup.vue'
  import { useRouter } from 'vue-router'

  const router = useRouter()

  const currentColor = inject('currentColor')
  const user = inject('user')
  const data = inject('data_pesanan')

  const editOpen = ref({})
  const editPrice = ref('')
  const editPetugas = ref('')

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

  const handleEdit = (item) => {
    editOpen.value = {}
    editOpen.value[item.id] = true
    editPrice.value = item.harga
    editPetugas.value = item.karyawan.id
  }
  const handleEditClose = () => {
    editOpen.value = {}
  }
  const handleSave = async (id) => {
    try {
      await httpClient.post('/edit_pesanan', {
        pesanan_id: id,
        harga: editPrice.value,
        karyawan_id: editPetugas.value,
      })
      await data_provider()
      editOpen.value = {}
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
        const resp = await httpClient.post('/pemesanan_list', {
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
  onMounted(() => {
    get_karyawan()
  })
</script>

<style scoped></style>
