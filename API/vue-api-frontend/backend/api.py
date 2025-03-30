from flask import Flask, request, jsonify
import pandas as pd
import os
from flask_cors import CORS

aplicacao = Flask(__name__)
CORS(aplicacao)

CAMINHO_ARQUIVO = os.path.join(
    "/media/sharlles/HD/Teste de Niverlamento/API/Relatorio/Relatorio_cadop.csv"
)
COLUNAS = [
    "id",
    "cnpj",
    "razao_social",
    "nome_fantasia",
    "tipo_empresa",
    "logradouro",
    "numero",
    "complemento",
    "bairro",
    "municipio",
    "uf",
    "cep",
    "ddd",
    "telefone",
    "telefone_2",
    "email",
    "nome_responsavel",
    "cargo_responsavel",
    "porte",
    "data_abertura"
]

try:
    if os.path.exists(CAMINHO_ARQUIVO):
        tabela_operadoras = pd.read_csv(CAMINHO_ARQUIVO, sep=",", on_bad_lines="skip")
    else:
        tabela_operadoras = pd.DataFrame()
        print(f'Arquivo CSV não encontrado no caminho: {CAMINHO_ARQUIVO}')
except Exception as e:
    tabela_operadoras = pd.DataFrame()
    print(f'Erro ao ler o arquivo CSV: {e}')

def processar_linha(linha):
    try:
        valores = linha.strip('"').split(';')
        resultado = {}
        for coluna, valor in zip(COLUNAS, valores):
            # Remove aspas extras e espaços em branco
            valor_limpo = valor.strip('"').strip()
            resultado[coluna] = valor_limpo if valor_limpo else None
            
        return resultado
    except Exception as e:
        print(f"Erro ao processar linha: {e}")
        return None

@aplicacao.route('/procurar', methods=['GET'])
def procurar_operadora():
    termo = request.args.get('q', '').lower()
    
    if not termo:
        return jsonify({"erro": "Informe o parâmetro de busca 'q' na URL."}), 400

    if tabela_operadoras.empty:
        return jsonify({"erro": "Arquivo CSV não carregado corretamente."}), 500

    resultados = tabela_operadoras[
        tabela_operadoras.apply(
            lambda linha: linha.astype(str).str.lower().str.contains(termo, na=False).any(),
            axis=1
        )
    ]

    # Processa cada linha e converte para o formato JSON desejado
    resultados_processados = []
    for _, linha in resultados.iterrows():
        linha_processada = processar_linha(str(linha.iloc[0]))
        if linha_processada:
            resultados_processados.append(linha_processada)

    return jsonify(resultados_processados)

if __name__ == '__main__':
    aplicacao.run(debug=True, port=5000)