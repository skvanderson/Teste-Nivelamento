methods: {
  async buscarOperadoras() {
    try {
      const response = await axios.get('http://localhost:5000/procurar', {
        params: { q: this.termoBusca }
      });
      this.operadoras = response.data;
    } catch (error) {
      console.error('Erro na busca:', error);
    }
  }
}
