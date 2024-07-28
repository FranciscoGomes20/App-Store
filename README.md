## Segue a baixo um guia para iniciar o projeto.

Primeiro crie um ambiente virtual utilizando o venv.
```python
python -m venv venv
```

Logo depois, acesse a pasta do ambiente pelo terminal e ative o arquivo "activate.bat".

```bash
venv\Scripts\activate
```

No caso do Linux
```bash
venv\bin\activate
```

## Instalando as dependências do projeto.

Use o gerenciador de pacotes do python para baixar as as bibliotecas necessárias do arquivo requirements.txt

```bash
pip install -r requirements.txt
```

## Migração do Banco de dados

Será necessário fazer uma migração no nosso banco de dados executando o seguinte comando:

```bash
python manage.py migrate
```

## Executando o projeto localmente.

Após abrir a pasta raiz do projeto (onde está o arquivo manage.py), com suas devidas dependências instaladas e dentro de um ambiente virtual (de preferência), execute o comando abaixo no terminal.

```bash
python manage.py runserver
```
Isso irá rodar o projeto em um servidor local, caso uma janela do navegador não se inicie sozinha, clique no link gerado no terminal.

## Contribuições

Pull Requests são bem-vindos.