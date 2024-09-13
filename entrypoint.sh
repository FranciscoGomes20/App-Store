#!/bin/sh

# Aguarda o banco de dados estar disponível
/wait-for-it.sh db:5432 --timeout=30 --strict -- echo "Database is up!"

# Executa as migrações
python manage.py migrate

# Inicia o servidor com o comando que foi passado (não repetir o runserver aqui)
exec "$@"
