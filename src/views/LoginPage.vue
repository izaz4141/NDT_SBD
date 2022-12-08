<template>
  <section class="justify-center items-center dark:text-white my-24">
    <form
      class="text-center my-10 text-sm md:text-xl relative items-center pt-8 pl-8 pr-8 pb-2 centerer rounded-lg bg-slate-200 dark:bg-main-dark-bg"
      @submit.prevent="handleSubmit"
    >
      <h1 class="text-center text-2xl mb-12 font-bold">SIGN IN</h1>
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
      <button
        type="submit"
        class="py-3 px-6 my-8 text-black dark:text-white font-semibold w-full"
        :style="{ background: currentColor }"
      >
        Login
      </button>
    </form>
  </section>
</template>

<script setup>
  import { ref, inject } from 'vue'
  import httpClient from '../api/api'
  import { useRouter } from 'vue-router'

  const router = useRouter()
  const user = inject('user')
  const user_id = inject('user_id')
  if (user.value) {
    router.push('/')
  }
  const currentColor = inject('currentColor')

  const email = ref('')
  const password = ref('')

  const user_provider = async () => {
    try {
      const resp = await httpClient.post('/@me', {
        user_id: user_id.value,
      })
      user.value = resp.data
    } catch (error) {
      user.value = false
      console.log('Not Authorized')
    }
  }

  const handleSubmit = async () => {
    try {
      const resp = await httpClient.post('/login', {
        email: email.value,
        password: password.value,
      })
      user_id.value = resp.data.id
      user_provider()
      router.push('/')
    } catch (error) {
      try {
        console.log(error)
        if (error.response.status === 401) {
          alert('Invalid Credentials')
        }
        if (error.response.status === 404) {
          alert('User not Found!')
        }
      } catch (er) {
        console.log(er)
      }
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
