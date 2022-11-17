<template>
  <div class="my-12">
    <h1 class="text-center justify-center flex mb-10 text-3xl font-extrabold">
      Pesan Layanan
    </h1>
    <form
      @submit.prevent="handleSubmit"
      class="text-center my-10 text-sm md:text-xl relative items-center pt-8 pl-8 pr-8 pb-2 centerer rounded-lg bg-slate-200 dark:bg-main-dark-bg"
    >
      <div class="form-row">
        <label html-for="name" class="form-label">Nama Lengkap</label>
        <div class="div-input">
          <input type="text" class="form-input" id="" v-model="nama" />
        </div>
      </div>
      <div class="form-row">
        <label htmlFor="email" class="form-label"> Email </label>
        <div class="div-input">
          <input type="email" class="form-input" id="" v-model="email" />
        </div>
      </div>
      <div class="form-row">
        <label htmlFor="text" class="form-label"> No Handphone </label>
        <div class="div-input">
          <input
            type="text"
            class="form-input"
            id=""
            v-model="no_telp"
            @keypress="isNumber($event)"
          />
        </div>
      </div>
      <div class="form-row">
        <label htmlFor="text" class="form-label"> Lokasi </label>
        <div class="div-input">
          <input type="text" class="form-input" id="" v-model="lokasi" />
        </div>
      </div>
      <div class="form-row">
        <label htmlFor="text" class="form-label"> Layanan </label>
        <select class="form-select" v-model="layanan">
          <option v-for="item in items" :value="item">
            {{ item }}
          </option>
        </select>
      </div>
      <div class="form-row">
        <label htmlFor="text" class="form-label"> Deskripsi Pekerjaan: </label>
        <div class="div-input">
          <textarea
            type="text"
            class="form-input min-h-[32vh] items-start"
            id=""
            v-model="deskripsi"
          />
        </div>
      </div>
      <button
        type="submit"
        class="py-3 px-6 my-8 text-black dark:text-white font-semibold w-full"
        :style="{ background: currentColor }"
      >
        Pesan
      </button>
    </form>
  </div>
</template>

<script setup>
  import { ref, inject } from 'vue'
  const user = inject('user')
  const currentColor = inject('currentColor')

  const nama = ref(user ? user.value.name : '')
  const email = ref(user ? user.value.email : '')
  const no_telp = ref(user ? user.value.no_telp : '')

  const lokasi = ref('')
  const layanan = ref('')
  const deskripsi = ref('')

  const items = ['gamma', 'xray', 'positron']

  const handleSubmit = async () => {
    try {
      await httpClient.post('/order', {
        name: nama.value,
        email: email.value,
        no_telp: no_telp.value,
        lokasi: lokasi.value,
        layanan: layanan.value,
        deskripsi: deskripsi.value,
      })
      router.push('/')
    } catch (error) {
      console.log(error)
    }
  }

  function isNumber(evt) {
    const keysAllowed = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+']
    const keyPressed = evt.key

    if (!keysAllowed.includes(keyPressed)) {
      evt.preventDefault()
    }
  }
</script>

<style scoped>
  .centerer {
    margin: 0 auto;
  }
  form {
    width: 75%;
  }
  .form-row {
    margin-top: 3vh;
    margin-bottom: 3vh;
  }
  .form-label {
    display: flex;
    justify-content: flex-start;
    margin-right: 2vw;
    font-weight: 500;
    padding-left: 0.3rem;
    font-size: 0.875rem /* 14px */;
    line-height: 1.25rem /* 20px */;
  }
  .form-input {
    width: 100%;
    --tw-text-opacity: 1;
    color: rgb(17 24 39 / var(--tw-text-opacity));
    background-color: transparent;
  }
  .dark .form-input {
    --tw-text-opacity: 1;
    color: rgb(255 255 255 / var(--tw-text-opacity));
  }
  .form-input:focus {
    outline: 2px solid transparent;
    outline-offset: 2px;
  }
  .div-input {
    display: flex;
    width: 100%;
    padding-top: 1vh;
    padding-bottom: 1vh;
    justify-content: flex-end;
    border-radius: 0.375rem;
    padding-left: 0.5rem;
    padding-right: 0.5rem;
    background-color: white;
  }
  .dark .div-input {
    --tw-text-opacity: 1;
    background-color: rgb(17 24 39 / var(--tw-bg-opacity));
  }
  .div-input:focus-within {
    outline-style: solid;
    outline-width: 2px;
    outline-color: v-bind(currentColor);
  }
  .form-select {
    width: 100%;
    padding-top: 1vh;
    padding-bottom: 1vh;
    border-radius: 0.375rem;
    padding-left: 0.5rem;
    padding-right: 0.5rem;
    background-color: white;
  }
  .dark .form-select {
    --tw-text-opacity: 1;
    background-color: rgb(17 24 39 / var(--tw-bg-opacity));
  }
</style>
