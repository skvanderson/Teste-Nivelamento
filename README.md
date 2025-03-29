# Testes de Nivelamento - Web Scraping, Transformação de Dados, Banco de Dados e API

Este repositório contém soluções para os testes de nivelamento, abordando tarefas de Web Scraping, Transformação de Dados, Banco de Dados e API.

## Estrutura do Projeto

```
testes-nivelamento-automacao/
│── Web_Scraping/
│   ├── scraper.py  # Script para baixar anexos PDF
│   ├── README.md  # Instruções sobre o Web Scraping
│
│── Transformacao_Dados/
│   ├── ExtrairTabelaPdf.py  # Script para extrair dados dos PDFs
│   ├── venv/  # Ambiente virtual (adicionado ao .gitignore)
│   ├── README.md  # Instruções sobre a transformação de dados
│
│── Banco_Dados/
│   ├── script_banco.py  # Script para manipulação de banco de dados
│   ├── README.md  # Instruções sobre banco de dados
│
│── API/
│   ├── api.py  # Script para interagir com a API
│   ├── README.md  # Instruções sobre API
│
│── .gitignore  # Arquivos e pastas a serem ignorados pelo Git
│── README.md  # Documentação geral do repositório
```

## 1. Web Scraping
O objetivo do teste de Web Scraping é baixar os anexos I e II da ANS e compactá-los em um arquivo ZIP.

### Execução
```bash
cd Web_Scraping
python scraper.py
```

## 2. Transformação de Dados
Este teste envolve a extração de dados de tabelas dos PDFs baixados, conversão para CSV e compactação do arquivo final.

### Execução
```bash
cd Transformacao_Dados
python ExtrairTabelaPdf.py
```

## 3. Banco de Dados
O teste de banco de dados envolve a manipulação de dados armazenados e consultas estruturadas.

### Execução
```bash
cd Banco_Dados
python script_banco.py
```

## 4. API
O teste de API consiste em interagir com um endpoint para enviar e receber dados.

### Execução
```bash
cd API
python api.py
```

## Configuração do Ambiente
Certifique-se de ter o Python instalado e instale as dependências:

```bash
pip install -r requirements.txt
```

## Contribuição
Sinta-se à vontade para abrir issues e PRs com melhorias!


