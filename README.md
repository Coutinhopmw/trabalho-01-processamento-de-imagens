# Máquina vritual

## Requisitos
- Python 3.x instalado
- Pip instalado
- Virtualenv instalado (caso não tenha, instale com `pip install virtualenv`)

## Configuração do Ambiente Virtual
1. Navegue até a pasta do projeto:
   ```sh
   cd caminho/do/projeto
   ```
2. Crie um ambiente virtual:
   ```sh
   python -m venv venv
   ```
3. Ative o ambiente virtual:
   - No Windows:
     ```sh
     venv\Scripts\activate
     ```
   - No macOS/Linux:
     ```sh
     source venv/bin/activate
     ```

## Instalação das Dependências
Após ativar o ambiente virtual, instale as dependências do projeto:
```sh
pip install -r requirements.txt
```
## Executar a aplicação
Após instalar as dependências, executar os comandos:
  python3 ampliacao.py
  python3 reducao.py
