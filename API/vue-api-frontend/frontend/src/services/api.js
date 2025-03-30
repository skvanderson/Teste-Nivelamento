import axios from 'axios';

const api = axios.create({
  baseURL: 'http://127.0.0.1:5000'
});

export const operadorasService = {
  async buscarOperadoras(termo) {
    try {
      const response = await api.get('/procurar', {
        params: {
          q: termo
        }
      });
      return response.data;
    } catch (error) {
      throw error;
    }
  }
};

export default operadorasService; 