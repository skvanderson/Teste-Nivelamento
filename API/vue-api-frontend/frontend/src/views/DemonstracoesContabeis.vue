<template>
  <div class="demonstracoes-contabeis">
    <h2>Demonstrações Contábeis</h2>
    
    <div class="search-container">
      <input 
        type="text" 
        v-model="dataBusca" 
        placeholder="Digite a data (formato: DD/MM/AAAA)"
        class="search-input"
      >
      <button @click="buscarPorData" class="search-button">Buscar</button>
    </div>

    <div v-if="loading" class="loading">
      Carregando...
    </div>

    <div v-else-if="erro" class="error">
      {{ erro }}
    </div>

    <div v-else-if="demonstracoes.length > 0" class="results">
      <table class="data-table">
        <thead>
          <tr>
            <th>Data</th>
            <th>Reg ANS</th>
            <th>Código Conta</th>
            <th>Descrição</th>
            <th>Saldo Inicial</th>
            <th>Saldo Final</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, index) in demonstracoes" :key="index">
            <td>{{ item.data }}</td>
            <td>{{ item.reg_ans }}</td>
            <td>{{ item.cd_conta_contabil }}</td>
            <td>{{ item.descricao }}</td>
            <td>{{ formatarValor(item.vl_saldo_inicial) }}</td>
            <td>{{ formatarValor(item.vl_saldo_final) }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import { demonstracoesContabeisApi } from '@/api/demonstracoesContabeis';

export default {
  name: 'DemonstracoesContabeis',
  data() {
    return {
      dataBusca: '',
      demonstracoes: [],
      loading: false,
      erro: null
    };
  },
  methods: {
    async buscarPorData() {
      if (!this.dataBusca) {
        this.erro = 'Por favor, digite uma data';
        return;
      }

      this.loading = true;
      this.erro = null;
      this.demonstracoes = [];

      try {
        const data = this.dataBusca.replace(/\//g, '');
        this.demonstracoes = await demonstracoesContabeisApi.buscarPorData(data);
      } catch (error) {
        this.erro = 'Erro ao buscar demonstrações contábeis. Tente novamente.';
        console.error('Erro:', error);
      } finally {
        this.loading = false;
      }
    },
    formatarValor(valor) {
      return new Intl.NumberFormat('pt-BR', {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
      }).format(valor);
    }
  }
};
</script>

<style scoped>
.demonstracoes-contabeis {
  padding: 20px;
}

.search-container {
  margin-bottom: 20px;
  display: flex;
  gap: 10px;
}

.search-input {
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
  width: 200px;
}

.search-button {
  padding: 8px 16px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.search-button:hover {
  background-color: #45a049;
}

.loading, .error {
  text-align: center;
  padding: 20px;
}

.error {
  color: red;
}

.data-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

.data-table th,
.data-table td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

.data-table th {
  background-color: #f4f4f4;
}

.data-table tr:nth-child(even) {
  background-color: #f9f9f9;
}

.data-table tr:hover {
  background-color: #f5f5f5;
}
</style> 