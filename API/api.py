from flask import Flask, request, jsonify
import pandas as pd
import os

# Criação da aplicação Flask
aplicacao = Flask(__name__)

# Caminho do arquivo CSV com os dados das operadoras
CAMINHO_ARQUIVO = os.path.join(
    "/media", "sharlles", "HD", "Teste de Niverlamento", "API", "Relatorio", "Relatorio_cadop.csv"
)

# Tenta carregar os dados do CSV
try:
    if os.path.exists(CAMINHO_ARQUIVO):  # Verifica se o arquivo existe
        tabela_operadoras = pd.read_csv(CAMINHO_ARQUIVO, sep=",", on_bad_lines="skip")
    else:
        tabela_operadoras = pd.DataFrame()
        print(f'Arquivo CSV não encontrado no caminho: {CAMINHO_ARQUIVO}')
except Exception as e:
    tabela_operadoras = pd.DataFrame()
    print(f"Erro ao ler o arquivo CSV: {e}")

# Rota para procurar operadoras por texto
@aplicacao.route('/procurar', methods=['GET'])
def procurar_operadora():
    termo = request.args.get('q', '').lower()
    if not termo:
        return jsonify({"erro": "Informe o parâmetro de busca 'q' na URL."}), 400

    if tabela_operadoras.empty:
        return jsonify({"erro": "Arquivo CSV ainda não foi carregado corretamente."}), 500

    # Filtra as linhas que contêm o termo em qualquer coluna
    resultados = tabela_operadoras[
        tabela_operadoras.apply(
            lambda linha: linha.astype(str).str.lower().str.contains(termo, na=False).any(),
            axis=1
        )
    ]

    return jsonify(resultados.to_dict(orient='records'))

# Inicia o servidor Flask
if __name__ == '__main__':
    aplicacao.run(debug=True)
