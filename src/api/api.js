import axios from 'axios'

const httpClient = axios.create({
  baseURL: 'https://atranzryou.pythonanywhere.com',
  // withCredentials: true,
})

export default httpClient
