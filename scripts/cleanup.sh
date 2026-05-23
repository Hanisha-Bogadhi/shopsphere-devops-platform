#!/bin/bash

echo "Cleaning Docker resources..."

docker compose down -v

docker system prune -a -f

docker volume prune -f

docker network prune -f

echo "Cleanup Completed Successfully"