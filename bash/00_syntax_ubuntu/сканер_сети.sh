#!/bin/bash
# Простой сканер портов
TARGET="10.0.2.15"

echo "Сканирование портов на $TARGET"
for port in 22 80 443 8080; do
    nc -z -w 1 $TARGET $port 2>/dev/null
    if [ $? -eq 0 ]; then
        echo "Порт $port открыт"
    fi
done
