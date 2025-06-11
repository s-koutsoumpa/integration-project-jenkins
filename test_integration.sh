#!/bin/bash

echo "Testing started..."
sleep 5
response=$(curl -s http://web:5000)

if echo "$response" | grep -q "Hello from MongoDB"; then
  echo "Successful Test"
  exit 0
else
  echo "Test failed"
  exit 1
fi
