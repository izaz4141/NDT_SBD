<template>
  <div class="my-6">
    <table class="flex flex-col justify-center m-auto">
      <thead class="w-full">
        <tr class="flex justify-around">
          <th class="w-[10vw]" scope="col">Id</th>
          <th class="w-[10vw]" scope="col">Nama</th>
          <th class="w-[10vw]" scope="col">Email</th>
          <th class="w-[9vw]" scope="col">Author Level</th>
          <th class="w-[15vw]" scope="col">Pemesanan</th>
          <th class="w-[10vw]" scope="col">Departemen</th>
          <th class="w-[15vw]" scope="col">Peminjaman</th>
          <th class="w-[15vw]" scope="col">Pekerjaan</th>
          <th class="w-[10vw]" scope="col">Tanggal Daftar</th>
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
          <!-- Nama -->
          <td class="w-[10vw] overflow-auto">
            <div>
              {{ item.name }}
            </div>
          </td>
          <!-- Email -->
          <td class="w-[10vw] overflow-auto">
            <div>
              {{ item.email }}
            </div>
          </td>
          <!-- Author Level -->
          <td class="w-[9vw] justify-center flex items-center overflow-auto">
            <div v-if="editOpen[item.id]">
              <input
                type="text"
                v-model="editAuthor_level"
                class="w-[6vw] px-[1vw] py-1 bg-white dark:bg-gray-900 rounded-md border-1 text-center"
                :style="{ borderColor: currentColor }"
                @keypress="isNumber"
              />
            </div>
            <div v-else>
              {{ item.author_level }}
            </div>
          </td>
          <!-- Pemesanan -->
          <td class="w-[15vw] justify-center flex items-center overflow-auto">
            <div>
              {{ item.pesanan.map((pesan) => pesan.layanan).join(', ') }}
            </div>
          </td>
          <!-- Departemen -->
          <td class="w-[10vw] justify-center flex items-center overflow-auto">
            <div v-if="editOpen[item.id]">
              <select
                class="px-4 py-1 bg-white dark:bg-gray-900 rounded-md border-1"
                v-model="editDepartemen"
              >
                <option v-for="dep in departemen" :value="dep.id">
                  {{ dep.name }}
                </option>
              </select>
            </div>
          </td>
          <!-- Peminjaman -->
          <td class="w-[15vw] justify-center flex items-center overflow-auto">
            <div>
              {{
                item.meminjam
                  .filter((pinjam) =>
                    pinjam.item.name == 'Barang Telah Dihapus' ? false : true,
                  )
                  .map((p) => p.item.name)
                  .join(', ')
              }}
            </div>
          </td>
          <!-- Pekerjaan -->
          <td class="w-[15vw] justify-center flex items-center overflow-auto">
            <div v-if="editOpen[item.id]">
              <select
                class="px-4 py-1 bg-white dark:bg-gray-900 rounded-md border-1"
                v-model="editPekerjaan"
              >
                <option v-for="kerja in pekerjaan" :value="kerja.id">
                  {{ kerja.lokasi }}
                </option>
              </select>
            </div>
            <div v-else>
              {{ item.pekerjaan.map((p) => p.lokasi).join(', ') }}
            </div>
          </td>
          <!-- Tanggal Daftar -->
          <td class="w-[10vw] justify-center flex items-center overflow-auto">
            {{ item.date_added }}
          </td>
          <td class="w-[20vw] justify-center flex items-center overflow-auto">
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
                class="text-3xl rounded-full h-min w-min absolute right-2"
              >
                <Icon icon="ic:twotone-cancel" />
              </button>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
  import { inject, onMounted, ref } from 'vue'
  import httpClient from '../api/api'
  import { Icon } from '@iconify/vue'

  const currentColor = inject('currentColor')
  const user = inject('user')
  const data = inject('data_dev_users')

  const editOpen = ref({})
  const editAuthor_level = ref('')
  const editDepartemen = ref('')
  const editPekerjaan = ref('')

  const pekerjaan = ref([])
  const departemen = ref([])

  function isNumber(evt) {
    const keysAllowed = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+']
    const keyPressed = evt.key

    if (!keysAllowed.includes(keyPressed)) {
      evt.preventDefault()
    }
  }

  const handleEdit = (item) => {
    editOpen.value = {}
    editOpen.value[item.id] = true
    editAuthor_level.value = item.author_level
    if (item.pekerjaan.id) {
      editPekerjaan.value = item.pekerjaan.id
    } else {
      editPekerjaan.value = 'bukan'
    }
    if (item.departemen) {
      editDepartemen.value = item.departemen.id
    } else {
      editDepartemen.value = 'bukan'
    }
  }
  const handleEditClose = () => {
    editOpen.value = {}
  }
  const handleSave = async (id) => {
    try {
      await httpClient.post('/edit_user_dev', {
        user_id: id,
        dev_author_level: user.value.author_level,
        author_level: parseInt(editAuthor_level.value),
        departemen_id: editDepartemen.value,
        pekerjaan_id: editPekerjaan.value,
      })
      await data_provider()
      editOpen.value = {}
    } catch (er) {
      console.log(er)
    }
  }

  const handleDelete = async (id) => {
    try {
      await httpClient.post('/remove_user', {
        user_id: id,
        author_level: user.value.author_level,
      })
      await data_provider()
    } catch (er) {
      console.log(er)
    }
  }
  const data_provider = async () => {
    if (user.value) {
      try {
        const resp = await httpClient.post('/dev_users_list', {
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
  const get_pekerjaan = async () => {
    if (user.value) {
      try {
        const resp = await httpClient.post('/pemesanan_list', {
          author_level: user.value.author_level,
        })
        pekerjaan.value = resp.data
      } catch (er) {
        console.log(er)
      }
    } else {
      router.push('/')
    }
  }
  const get_departemen = async () => {
    try {
      const resp = await httpClient.get('/departemen_list')
      departemen.value = resp.data
    } catch (er) {
      console.log(er)
    }
  }
  const handleCopy = (id) => {
    navigator.clipboard.writeText(id)
  }
  onMounted(async () => {
    await get_pekerjaan()
    await get_departemen()
  })
</script>

<style scoped></style>
