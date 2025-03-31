# Testes de Nivelamento - Web Scraping, Transformação de Dados, Banco de Dados e API

Este repositório contém soluções para os testes de nivelamento, abordando tarefas de Web Scraping, Transformação de Dados, Banco de Dados e API.

## Estrutura do Projeto

```
teste-nivelamento/
├── Web_Scraping/
│   ├── scraper.py
│   ├── requirements.txt
│
├── Transformacao_Dados/
│   ├── ExtrairTabelaPdf.py
│   ├── requirements.txt
│
├── Banco_Dados/
│   ├── test_Query.sql     
│
├── API/
│   ├── api.py
│   ├── requirements.txt
│   ├── postman/
│   │   └── Operadoras_API.postman_collection.json
│   └── README.md
│
├── .gitignore
└── README.md

```

## 1. Web Scraping
O objetivo do teste de Web Scraping é baixar os anexos I e II da ANS e compactá-los em um arquivo ZIP.
Pré-requisitos
Python 3.8+

Bibliotecas: requests, BeautifulSoup4, zipfile

### Instalação
```bash
cd Web_Scraping
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou .\venv\Scripts\activate no Windows
pip install -r requirements.txt
```
### Execução
```python scraper.py```

## 2. Transformação de Dados
Este teste envolve a extração de dados de tabelas dos PDFs baixados, conversão para CSV e compactação do arquivo final.

### Instalação
```bash
cd ../Transformacao_Dados
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### Execução
```bash
python ExtrairTabelaPdf.py
```

## 3. Banco de Dados
O teste de banco de dados envolve a manipulação de dados armazenados e consultas estruturadas.

### Execução
```bash
cd Teste de Banco de Dados
Test_Query.sqç
```

## 4. API
O teste de API consiste em interagir com um endpoint para enviar e receber dados.

### Inicialização
```bash
cd ../API
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Execução
```bash
cd ../API
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### Endpoints
Método	Endpoint	Parâmetro	Exemplo
GET	/procurar	q	/procurar?q=saude

### Exemplo de Uso:
```bash
curl "http://localhost:5000/procurar?q=unimed" | jq
```

## Configuração do Ambiente
Certifique-se de ter o Python instalado e instale as dependências:

```bash
pip install -r requirements.txt
```

## Contribuição
Sinta-se à vontade para abrir issues e PRs com melhorias!


