import axios from 'axios'

const httpClient = axios.create({
  baseURL: 'http://localhost:5055',
  withCredentials: true,
})

export default httpClient
