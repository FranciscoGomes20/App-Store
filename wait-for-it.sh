#!/usr/bin/env bash

# Simple script to wait for a service to become available
# Usage: ./wait-for-it.sh host:port -- command arguments

set -e

TIMEOUT=30
QUIET=0
PROTOCOL="tcp"

print_help() {
  echo "Usage: $0 host:port [--timeout SECONDS] [--quiet] -- command args"
  echo
  echo "Options:"
  echo "  --timeout SECONDS  How long to wait for the service to be available"
  echo "  --quiet            Suppress output"
  echo "  --protocol PROTOCOL  Protocol to use (tcp or http)"
  echo "  --help             Display this help message"
}

while [[ $# -gt 0 ]]; do
  case $1 in
    *:* )
      HOST_PORT=(${1//:/ })
      HOST=${HOST_PORT[0]}
      PORT=${HOST_PORT[1]}
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
    --protocol)
      PROTOCOL=$2
      shift 2
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
  if [ "$PROTOCOL" = "tcp" ]; then
    nc -z $HOST $PORT && break
  elif [ "$PROTOCOL" = "http" ]; then
    curl -s $HOST:$PORT > /dev/null && break
  else
    echo "Unsupported protocol: $PROTOCOL"
    exit 1
  fi
  sleep 1
done

if [ "$QUIET" -eq 0 ]; then
  echo "$HOST:$PORT is available."
fi

exec $COMMAND
