#!/bin/sh

# Extrai o host e a porta da variável DATABASE_URL
DB_HOST=$(echo "$DATABASE_URL" | sed -e 's/^.*@//g' -e 's/:.*//g')
DB_PORT=$(echo "$DATABASE_URL" | sed -e 's/^.*://g' -e 's/\/.*//g')

# Para fins de depuração, você pode imprimir o host e a porta
echo "DB_HOST: $DB_HOST"
echo "DB_PORT: $DB_PORT"

# Espera o banco de dados ficar disponível
/wait-for-it.sh "$DB_HOST":"$DB_PORT" --timeout=30 --strict -- echo "Database is up!"

# Executa as migrações
python manage.py migrate

# Inicia o servidor com o comando que foi passado (não repetir o runserver aqui)
exec "$@"
