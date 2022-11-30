<template>
  <div class="my-6">
    <table class="flex flex-col justify-center w-[90%] m-auto">
      <thead class="w-full">
        <tr class="flex justify-around">
          <th class="w-[10%]" scope="col">Id</th>
          <th class="w-[20%]" scope="col">Nama</th>
          <th class="w-[20%]" scope="col">Tipe</th>
          <th class="w-[10%]" scope="col">Status</th>
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
          <td class="w-[20%] overflow-auto">
            <div v-if="editOpen[item.id]">
              <input
                type="text"
                v-model="editName"
                class="px-4 py-1 bg-white dark:bg-gray-900 rounded-md border-1"
                :style="{ borderColor: currentColor }"
              />
            </div>
            <div v-else>
              {{ item.name }}
            </div>
          </td>
          <td class="w-[20%] overflow-auto">
            <div v-if="editOpen[item.id]">
              <input
                type="text"
                v-model="editTipe"
                class="px-4 py-1 bg-white dark:bg-gray-900 rounded-md border-1"
                :style="{ borderColor: currentColor }"
              />
            </div>
            <div v-else>
              {{ item.tipe }}
            </div>
          </td>
          <td class="w-[10%] justify-center flex items-center overflow-auto">
            <button
              v-if="item.peminjaman.id"
              disabled
              class="bg-violet-500 hover:bg-violet-400 text-white font-bold py-1 px-2 rounded-t brightness-50 cursor-not-allowed"
            >
              Dipinjam
            </button>
            <button
              v-else
              @click="handlePinjam(item.id)"
              class="bg-violet-500 hover:bg-violet-400 text-white font-bold py-1 px-2 rounded-t"
            >
              Pinjam
            </button>
          </td>
          <td class="w-[20%]">
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
                class="text-3xl rounded-full h-min w-min absolute right-4"
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
  import { inject, ref } from 'vue'
  import httpClient from '../api/api'
  import { Icon } from '@iconify/vue'

  const currentColor = inject('currentColor')
  const user = inject('user')
  const data = inject('data_alat')

  const editOpen = ref({})
  const editName = ref('')
  const editTipe = ref('')

  const handleEdit = (item) => {
    editOpen.value = {}
    editOpen.value[item.id] = true
    editName.value = item.name
    editTipe.value = item.tipe
  }
  const handleEditClose = () => {
    editOpen.value = {}
  }
  const handleSave = async (id) => {
    try {
      await httpClient.post('/edit_inventaris', {
        item_id: id,
        name: editName.value,
        tipe: editTipe.value,
      })
      await data_provider()
      editOpen.value = {}
    } catch (er) {
      console.log(er)
    }
  }

  const handleDelete = async (id) => {
    try {
      await httpClient.post('/remove_inventaris', {
        item_id: id,
      })
      await data_provider()
    } catch (er) {
      console.log(er)
    }
  }
  const data_provider = async () => {
    if (user.value) {
      try {
        const resp = await httpClient.post('/inventaris_list', {
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
  const handlePinjam = async (id) => {
    try {
      await httpClient.post('/meminjam', {
        item_id: id,
        user_id: user.value.id,
      })
      await data_provider()
    } catch (er) {
      console.log(er)
    }
  }
</script>

<style scoped></style>
