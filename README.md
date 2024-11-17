# Tradutor de Textos
Um programa de linha de comando que extrai texto de páginas web, traduz para um idioma especificado utilizando **Azure AI** e permite salvar a tradução. 

## Instalação e Execução
1. Clone este repositório:
   ```bash
   git clone https://github.com/ja1steinert/azure-ai-translator.git
   ```
2. Navegue para o diretório:
   ```bash
   cd azure-ai-translator
   ```
3. Instale as depedências:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure suas credenciais no arquivo .env:
   ```bash
    AZURE_ENDPOINT="YOUR_AZURE_ENDPOINT"
    API_KEY="YOUR_API_KEY"
    API_VERSION="YOUR_API_VERSION"
    DEPLOYMENT_NAME="YOUR_DEPLOYMENT_NAME"
   ```
5. Execute o programa:
   ```bash
   python app.py
   ```
