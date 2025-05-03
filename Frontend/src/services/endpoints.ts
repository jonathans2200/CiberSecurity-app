import axiosInstance from '@/services/axiosInstance';

async function uploadFile(file: File): Promise<any> {
  const formData = new FormData();
  formData.append('file', file);

  const token = 'Bearer ' + localStorage.getItem('access_token');
  console.log('Respuesta:', token);

  try {
    const response = await axiosInstance.post('analyze?type=file', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
        Authorization: `Bearer ${token}`,
      },
    });
    console.log('Respuesta:', response.data);
    return response.data;
  } catch (error) {
    console.error('Error al subir el archivo:', error);
    throw error;
  }
}
