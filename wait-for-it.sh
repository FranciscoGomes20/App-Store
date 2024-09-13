#!/usr/bin/env sh

# Simple script to wait for a service to become available
# Usage: ./wait-for-it.sh host:port -- command args

set -e

TIMEOUT=30
QUIET=0

print_help() {
  echo "Usage: $0 host:port [--timeout SECONDS] [--quiet] -- command args"
}

while [ $# -gt 0 ]; do
  case "$1" in
    *:* )
      HOST=$(echo "$1" | cut -d: -f1)
      PORT=$(echo "$1" | cut -d: -f2)
      shift
      ;;
    --timeout)
      TIMEOUT=$2
      shift 2
      ;;
    --quiet)
      QUIET=1
      shift
      ;;
    --help)
      print_help
      exit 0
      ;;
    *)
      COMMAND=$@
      break
      ;;
  esac
done

if [ -z "$HOST" ] || [ -z "$PORT" ]; then
  echo "Error: host and port are required"
  print_help
  exit 1
fi

echo "Waiting for $HOST:$PORT to be available..."

for i in $(seq $TIMEOUT); do
  nc -z $HOST $PORT && break
  echo "Waiting for $HOST:$PORT..."
  sleep 1
done

if [ "$i" = "$TIMEOUT" ]; then
  echo "Timeout: Unable to connect to $HOST:$PORT"
  exit 1
fi

exec $COMMAND
