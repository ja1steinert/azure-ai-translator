import requests
from bs4 import BeautifulSoup
from langchain_openai.chat_models.azure import AzureChatOpenAI
from dotenv import load_dotenv
import os


load_dotenv()
cliente = AzureChatOpenAI(
    azure_endpoint=os.getenv("AZURE_ENDPOINT"),
    api_key=os.getenv("API_KEY"),
    api_version=os.getenv("API_VERSION"),
    deployment_name=os.getenv("DEPLOYMENT_NAME"),
    max_retries=0
)

def extrair_texto_da_pagina(url):
    print("\n[INFO] Extraindo texto da página...")
    try:
        response = requests.get(url, timeout=10)
    except requests.RequestException as e:
        print(f"[ERRO] Não foi possível acessar a página: {e}")
        return None

    if response.status_code != 200:
        print(f"[ERRO] Código de status ao acessar a página: {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    # Removendo scripts e estilos
    for script_or_style in soup(["script", "style"]):
        script_or_style.decompose()

    texto = soup.get_text(separator=' ')
    linhas = (linha.strip() for linha in texto.splitlines())
    frases = (frase.strip() for linha in linhas for frase in linha.split(' '))
    texto = '\n'.join(frase for frase in frases if frase)

    return texto

def traduzir_texto(texto, lingua):
    print("\n[INFO] Traduzindo texto...")
    mensagens = [
        ("system", "Você atua como tradutor de textos"),
        ("user", f'Traduza "{texto}" para o idioma "{lingua}"')
    ]

    try:
        response = cliente.invoke(mensagens)
        return response.content
    except Exception as e:
        print(f"[ERRO] Ocorreu um erro durante a tradução: {e}")
        return None

def main():
    print("-- Tradutor de Textos --")
    print("1. Traduzir texto de uma URL")
    print("2. Sair")
    
    while True:
        opcao = input("\nEscolha uma opção (1 ou 2): ")
        if opcao == "1":
            url_texto = input("\nInsira a URL do texto a ser traduzido: ")
            idioma_destino = input("Insira o idioma para tradução (ex: Português, Espanhol, Inglês): ")
            
            texto = extrair_texto_da_pagina(url_texto)
            if texto:
                traducao = traduzir_texto(texto, idioma_destino)
                if traducao:
                    print("\n[TRADUÇÃO]")
                    print(traducao)
                    salvar = input("\nDeseja salvar a tradução em um arquivo? (s/n): ")
                    if salvar.lower() == "s":
                        with open("traducao.txt", "w", encoding="utf-8") as f:
                            f.write(traducao)
                        print("\n[INFO] Tradução salva como 'traducao.txt'.")
        elif opcao == "2":
            print("\n[INFO] Encerrando o programa.")
            break
        else:
            print("[ERRO] Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
