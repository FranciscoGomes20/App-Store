#!/bin/sh

# Extrai o host e a porta a partir da variável DATABASE_URL
DB_HOST=$(echo $DATABASE_URL | awk -F[/:] '{print $4}')
DB_PORT=$(echo $DATABASE_URL | awk -F[/:] '{print $5}')

# Espera o banco de dados ficar disponível
/wait-for-it.sh $DB_HOST:$DB_PORT --timeout=30 --strict -- echo "Database is up!"

# Executa as migrações
python manage.py migrate

# Inicia o servidor com o comando que foi passado (não repetir o runserver aqui)
exec "$@"
