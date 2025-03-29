import requests
import pdfplumber
import pandas as pd
import zipfile
import os

# URL do PDF
pdf_url = "https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536_RN537_RN538_RN539_RN541_RN542_RN544_546_571.pdf"
pdf_path = "Rol_Procedimentos.pdf"

def baixar_pdf(url, destino):
    """Baixa o PDF e salva no destino especificado."""
    response = requests.get(url)
    if response.status_code == 200:
        with open(destino, "wb") as f:
            f.write(response.content)
        print("✅ PDF baixado com sucesso!")
    else:
        raise Exception(f"Erro ao baixar PDF: {response.status_code}")

def extrair_tabelas_formatadas(pdf_path):
    """Extrai tabelas do PDF e formata corretamente os dados."""
    dados = []
    with pdfplumber.open(pdf_path) as pdf:
        for pagina in pdf.pages:
            tabelas = pagina.extract_tables()
            for tabela in tabelas:
                if tabela:
                    for linha in tabela:
                        linha_formatada = [cell.replace("\n", " ").strip() if cell else "" for cell in linha]
                        if any(linha_formatada):  # Exclui linhas completamente vazias
                            dados.append(linha_formatada)
    return dados

def ajustar_tabela(df):
    """Ajusta a tabela e remove repetição do cabeçalho."""
    cabecalho = df.iloc[0].tolist()  # Salva o cabeçalho original
    df.columns = cabecalho  # Define a primeira linha como cabeçalho
    df = df[1:].reset_index(drop=True)  # Remove a linha duplicada do cabeçalho

    # Remover repetições do cabeçalho
    df = df[df.apply(lambda linha: list(linha) != cabecalho, axis=1)].reset_index(drop=True)

    # Substituir abreviações
    substituicoes = {"OD": "Órteses e Próteses", "AMB": "Procedimentos Ambulatoriais"}
    df.rename(columns=substituicoes, inplace=True)
    return df

def remover_cabecalho_repetido(df, intervalo=20):
    """Remove cabeçalhos repetidos com base no intervalo especificado."""
    cabecalho = df.iloc[0].tolist()
    linhas_para_manter = df.apply(lambda linha: list(linha) != cabecalho, axis=1)
    for indice in range(intervalo, len(df), intervalo):
        linhas_para_manter[indice] = False  # Marca as linhas do cabeçalho como inválidas
    df = df[linhas_para_manter].reset_index(drop=True)
    return df

def exportar_csv(df, nome_base):
    """Exporta a tabela para CSV."""
    csv_path = f"{nome_base}.csv"
    df.to_csv(csv_path, index=False, encoding="utf-8-sig")
    print("📄 CSV gerado com sucesso!")
    return csv_path

def compactar_em_zip(arquivos, zip_filename):
    """Compacta múltiplos arquivos em um único arquivo ZIP."""
    with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
        for arquivo in arquivos:
            zipf.write(arquivo, os.path.basename(arquivo))
            os.remove(arquivo)  # Remove os arquivos originais
    print(f"📦 Compactação concluída: {zip_filename}")

def processo_principal():
    """Executa o fluxo completo de extração, formatação e compactação."""
    baixar_pdf(pdf_url, pdf_path)
    dados = extrair_tabelas_formatadas(pdf_path)
    
    if dados:
        df = pd.DataFrame(dados)
        df = ajustar_tabela(df)  # Ajusta a tabela e remove problemas de formatação
        df = remover_cabecalho_repetido(df, intervalo=20)  # Remove cabeçalhos repetidos a cada 20 linhas

        nome_base = "Rol_Procedimentos"
        csv_path = exportar_csv(df, nome_base)  # Exporta para CSV

        # Compacta o CSV e o PDF em ZIP
        zip_filename = f"{nome_base}.zip"
        compactar_em_zip([csv_path, pdf_path], zip_filename)

        print(f"✅ Processo finalizado! Arquivo ZIP gerado: {zip_filename}")
    else:
        print("⚠️ Nenhuma tabela válida encontrada no PDF.")

if __name__ == "__main__":
    processo_principal()
