# API de Busca de Operadoras

Esta API foi desenvolvida para buscar informações sobre as operadoras de planos de saúde em um arquivo CSV. Ela fornece um endpoint para realizar buscas por diferentes critérios nas informações das operadoras.

## Requisitos

- Python 3.x
- Flask
- Flask-CORS
- Pandas

## Instalação

1. Clone o repositório ou baixe os arquivos
2. Crie um ambiente virtual:
```bash
python3 -m venv venv
```

3. Ative o ambiente virtual:
```bash
# No Linux/Mac:
source venv/bin/activate
# No Windows:
.\venv\Scripts\activate
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Configuração

A API espera encontrar um arquivo CSV com as informações das operadoras no seguinte caminho:
```
/media/sharlles/HD/Teste de Niverlamento/API/Relatorio/Relatorio_cadop.csv
```

O arquivo CSV deve conter as seguintes colunas:
- id
- cnpj
- razao_social
- nome_fantasia
- tipo_empresa
- logradouro
- numero
- complemento
- bairro
- municipio
- uf
- cep
- ddd
- telefone
- telefone_2
- email
- nome_responsavel
- cargo_responsavel
- porte
- data_abertura

## Executando a API

Para iniciar a API, execute:
```bash
python api.py
```

A API estará disponível em `http://127.0.0.1:5000`

## Endpoints

### GET /procurar

Busca operadoras com base em um termo de pesquisa.

**Parâmetros:**
- `q` (query string): Termo de busca (obrigatório)

**Exemplo de requisição:**
```
http://127.0.0.1:5000/procurar?q=unimed
```

**Resposta de sucesso (200 OK):**
```json
[
  {
    "id": "419761",
    "cnpj": "19541931000125",
    "razao_social": "18 DE JULHO ADMINISTRADORA DE BENEFÍCIOS LTDA",
    "nome_fantasia": null,
    "tipo_empresa": "Administradora de Benefícios",
    "logradouro": "RUA CAPITÃO MEDEIROS DE REZENDE",
    "numero": "274",
    "complemento": null,
    "bairro": "PRAÇA DA BANDEIRA",
    "municipio": "Além Paraíba",
    "uf": "MG",
    "cep": "36660000",
    "ddd": "32",
    "telefone": "34624649",
    "telefone_2": null,
    "email": "contabilidade@cbnassessoria.com.br",
    "nome_responsavel": "LUIZ HENRIQUE MARENDINO GONÇALVES",
    "cargo_responsavel": "SÓCIO ADMINISTRADOR",
    "porte": "6",
    "data_abertura": "2015-05-19"
  }
]
```

**Códigos de erro:**
- 400 Bad Request: Quando o parâmetro de busca não é fornecido
- 500 Internal Server Error: Quando há problemas ao carregar o arquivo CSV

## Funcionalidades

- Busca case-insensitive (não diferencia maiúsculas de minúsculas)
- Busca em todas as colunas do CSV
- Retorna resultados em formato JSON estruturado
- Suporte a CORS para integração com frontend
- Tratamento de valores nulos/vazios

## Exemplo de Uso com Postman

Uma collection do Postman está disponível no arquivo `Operadoras_API.postman_collection.json`. Para importar:

1. Abra o Postman
2. Clique em "Import"
3. Arraste o arquivo `Operadoras_API.postman_collection.json` ou navegue até ele
4. Clique em "Import"

## Desenvolvimento

A API foi desenvolvida usando:
- Flask para o servidor web
- Pandas para manipulação de dados
- Flask-CORS para suporte a requisições cross-origin

## Contribuição

Para contribuir com o projeto:
1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Crie um Pull Request 