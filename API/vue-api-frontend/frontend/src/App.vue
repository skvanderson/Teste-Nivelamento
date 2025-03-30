<template>
  <div id="app">
    <h1>Busca de Operadoras</h1>
    <div class="search-container">
      <input 
        v-model="searchTerm" 
        type="text" 
        placeholder="Digite o nome da operadora"
        @keyup.enter="buscarOperadoras"
      >
      <button @click="buscarOperadoras">Buscar</button>
    </div>

    <div v-if="loading" class="loading">
      Carregando...
    </div>

    <div v-if="error" class="error">
      {{ error }}
    </div>

    <div v-if="operadoras.length > 0" class="results">
      <h2>Resultados:</h2>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Nome Fantasia</th>
              <th>Razão Social</th>
              <th>CNPJ</th>
              <th>Tipo</th>
              <th>Endereço</th>
              <th>Contato</th>
              <th>Responsável</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="operadora in operadoras" :key="operadora.id">
              <td>{{ operadora.nome_fantasia }}</td>
              <td>{{ operadora.razao_social }}</td>
              <td>{{ operadora.cnpj }}</td>
              <td>{{ operadora.tipo_empresa }}</td>
              <td>
                {{ operadora.logradouro }}, {{ operadora.numero }}
                {{ operadora.complemento ? `- ${operadora.complemento}` : '' }}
                <br>
                {{ operadora.bairro }} - {{ operadora.municipio }}/{{ operadora.uf }}
                <br>
                CEP: {{ operadora.cep }}
              </td>
              <td>
                ({{ operadora.ddd }}) {{ operadora.telefone }}
                {{ operadora.telefone_2 ? `<br>(${operadora.ddd}) ${operadora.telefone_2}` : '' }}
                <br>
                {{ operadora.email }}
              </td>
              <td>
                {{ operadora.nome_responsavel }}
                <br>
                {{ operadora.cargo_responsavel }}
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import operadorasService from './services/api';

export default {
  name: 'App',
  data() {
    return {
      searchTerm: '',
      operadoras: [],
      loading: false,
      error: null
    }
  },
  methods: {
    async buscarOperadoras() {
      if (!this.searchTerm.trim()) {
        this.error = 'Por favor, digite um termo para busca';
        return;
      }

      this.loading = true;
      this.error = null;
      this.operadoras = [];

      try {
        const response = await operadorasService.buscarOperadoras(this.searchTerm);
        this.operadoras = response;
      } catch (error) {
        this.error = 'Erro ao buscar operadoras. Tente novamente.';
        console.error('Erro:', error);
      } finally {
        this.loading = false;
      }
    }
  }
}
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.search-container {
  margin: 20px 0;
  display: flex;
  gap: 10px;
}

input {
  flex: 1;
  padding: 8px;
  font-size: 16px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

button {
  padding: 8px 16px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}

.loading {
  text-align: center;
  margin: 20px 0;
}

.error {
  color: red;
  margin: 20px 0;
}

.results {
  margin-top: 20px;
}

.table-container {
  overflow-x: auto;
  margin-top: 20px;
}

table {
  width: 100%;
  border-collapse: collapse;
  background-color: white;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
}

th, td {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

th {
  background-color: #f5f5f5;
  font-weight: bold;
}

tr:hover {
  background-color: #f9f9f9;
}

td {
  vertical-align: top;
}

@media screen and (max-width: 768px) {
  .table-container {
    margin: 0 -20px;
  }
  
  table {
    font-size: 14px;
  }
  
  th, td {
    padding: 8px;
  }
}
</style>