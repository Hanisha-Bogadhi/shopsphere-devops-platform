#!/bin/bash

echo "Starting ShopSphere DevOps Platform..."

docker compose up --build -d

echo "Application Started Successfully"

echo "Frontend: http://localhost:3001"
echo "Product Service: http://localhost:5001"
echo "Cart Service: http://localhost:5000"