from flask import Flask, request, jsonify
import pandas as pd
import os
from flask_cors import CORS  # Linha 4

# Nome da variável corrigido
aplicacao = Flask(__name__)  # Linha 7 - Corrigido de api.tacao para aplicacao
CORS(aplicacao)

# Nome da variável do caminho corrigido
CAMINHO_ARQUIVO = os.path.join(  # Linha 11 - Corrigido CAITINHO_ARQUIVO
    "/media/sharlles/HD/Teste de Niverlamento/API/Relatorio/Relatorio_cadop.csv"
)

try:
    if os.path.exists(CAMINHO_ARQUIVO):
        tabela_operadoras = pd.read_csv(CAMINHO_ARQUIVO, sep=",", on_bad_lines="skip")
    else:
        tabela_operadoras = pd.DataFrame()
        print(f'Arquivo CSV não encontrado no caminho: {CAMINHO_ARQUIVO}')
except Exception as e:
    tabela_operadoras = pd.DataFrame()
    print(f'Erro ao ler o arquivo CSV: {e}')

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

    return jsonify(resultados.to_dict(orient='records'))

if __name__ == '__main__':
    aplicacao.run(debug=True, port=5000)