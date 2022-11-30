<template>
  <section class="justify-center items-center dark:text-white my-12">
    <form
      class="text-center my-10 text-sm md:text-xl relative items-center pt-8 pl-8 pr-8 pb-2 centerer rounded-lg bg-slate-200 dark:bg-main-dark-bg"
      @submit.prevent="handleSubmit"
    >
      <h2 class="text-center text-2xl font-bold">SIGN UP</h2>
      <div class="form-row">
        <label htmlFor="name" class="form-label"> User Name </label>
        <div class="div-input">
          <input type="name" class="form-input" id="" v-model="name" />
        </div>
      </div>
      <div class="form-row">
        <label htmlFor="email" class="form-label"> Email </label>
        <div class="div-input">
          <input type="email" class="form-input" id="" v-model="email" />
        </div>
      </div>
      <div class="form-row">
        <label htmlFor="password" class="form-label"> Password </label>
        <div class="div-input">
          <input type="password" class="form-input" id="" v-model="password" />
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
      <button
        type="submit"
        class="py-3 px-6 my-8 bg-white dark:bg-main-dark-bg text-black dark:text-white w-full"
        :style="{ background: currentColor }"
      >
        Register
      </button>
    </form>
  </section>
</template>

<script setup>
  import { ref, inject } from 'vue'
  import { useRouter } from 'vue-router'
  import httpClient from '../api/api'

  const router = useRouter()
  const user = inject('user')
  if (user.value) {
    router.push('/')
  }
  const currentColor = inject('currentColor')

  const name = ref('')
  const email = ref('')
  const password = ref('')
  const no_telp = ref('')

  const user_provider = async () => {
    try {
      const resp = await httpClient.get('/@me')
      user.value = resp.data
    } catch (error) {
      console.log('Not Authorized')
    }
  }
  const handleSubmit = async () => {
    try {
      await httpClient.post('/register', {
        name: name.value,
        email: email.value,
        password: password.value,
        no_telp: no_telp.value,
      })
      user_provider()
      router.push('/')
    } catch (error) {
      try {
        if (error.response.status === 409) {
          alert('Akun lain telah memakai email tersebut')
        }
      } catch (er) {
        console.log(er)
      }
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

<style lang="css" scoped>
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
    margin-right: 2vh;
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
</style>
