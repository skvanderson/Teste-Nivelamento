import requests  
from bs4 import BeautifulSoup  
import os  
import zipfile 

URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

def obter_links_pdfs(url):
    resposta = requests.get(url)
    pagina_html = BeautifulSoup(resposta.text, "html.parser")
    
    links_pdfs = []
    for link in pagina_html.find_all("a", href=True):
        href = link["href"]
        if href.endswith(".pdf"):
            if href.startswith("/"): 
                href = "https://www.gov.br" + href
            links_pdfs.append(href)
    
    return links_pdfs

def baixar_pdfs(links_pdfs, caminho_salvar="downloads"):
    if not os.path.exists(caminho_salvar):
        os.makedirs(caminho_salvar)
    
    arquivos_baixados = []
    for link in links_pdfs:
        nome_arquivo = os.path.join(caminho_salvar, os.path.basename(link))
        resposta = requests.get(link)
        if resposta.status_code == 200 and "Anexo" in nome_arquivo:
            with open(nome_arquivo, "wb") as arquivo:
                arquivo.write(resposta.content)
            
                arquivos_baixados.append(nome_arquivo)
                print(f"Baixado: {nome_arquivo}")
    return arquivos_baixados

def compactar_pdfs(arquivos, pasta="downloads", nome_zip="downloads/anexos.zip"):
    with zipfile.ZipFile(nome_zip, "w") as arquivo_zip:
        for arquivo in arquivos:
            if os.path.exists(arquivo):  
                arquivo_zip.write(arquivo, os.path.basename(arquivo))
                os.remove(arquivo)  
    print(f"Arquivos compactados em {nome_zip}")

pdfs = obter_links_pdfs(URL) 
if pdfs:
    arquivos_baixados = baixar_pdfs(pdfs)
    if arquivos_baixados:
        compactar_pdfs(arquivos_baixados)
    else:
        print("Nenhum arquivo foi baixado, compactação cancelada.")
else:
    print("Nenhum PDF encontrado no site.")

