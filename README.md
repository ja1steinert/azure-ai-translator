# Web Text Translator
A command-line program that extracts text from web pages, translates it into a specified language using **Azure AI**, and allows saving the translation.

## Installation and Execution
1. Clone this repository:
   ```bash
   git clone https://github.com/ja1steinert/azure-ai-translator.git
   ```
2. Navigate to directory:
   ```bash
   cd azure-ai-translator
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure your credentials in the .env file:
   ```bash
    AZURE_ENDPOINT="YOUR_AZURE_ENDPOINT"
    API_KEY="YOUR_API_KEY"
    API_VERSION="YOUR_API_VERSION"
    DEPLOYMENT_NAME="YOUR_DEPLOYMENT_NAME"
   ```
5. Run the program:
   ```bash
   python app.py
   ```
Fun fact: This README was translated to English using this application :P
