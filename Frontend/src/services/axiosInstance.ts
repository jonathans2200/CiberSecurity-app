import axios from 'axios';

// const axiosInstance = axios.create({
//   baseURL: 'http://127.0.0.1:8000/', // Base URL de tu API
//   headers: {
//     Accept: 'application/json',
//   },
// });

const baseURL = import.meta.env.VITE_API_URL
  || '/'

const axiosInstance = axios.create({
  baseURL,
  headers: { Accept: 'application/json',
             Authorization: `BEARER ${localStorage.getItem('access_token')}` },
})

export default axiosInstance;

