#!/bin/bash
set -e
# Build and start containers
docker-compose up -d --build

# Wait for PostgreSQL to be up
until docker exec $(docker-compose ps -q db) pg_isready -U inventory_user; do
  echo "Waiting for PostgreSQL to be ready..."
  sleep 2
done

# Load schema if it's present
if [ -f schema.sql ]; then
  cat schema.sql | docker exec -i $(docker-compose ps -q db) psql -U inventory_user -d inventory_db
fi

echo "Setup complete. FastAPI available on http://localhost:8000/"
