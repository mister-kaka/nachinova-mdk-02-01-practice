#!/bin/bash
# Проверяет доступность хоста

read -p "Введите адрес (google.com или IP): " host

echo "Проверяем соединение с $host..."
echo "------------------------"

ping -c 4 -W 2 "$host" | while read line; do
    if echo "$line" | grep -q "bytes from"; then
        time=$(echo "$line" | grep -o "time=[0-9.]*" | cut -d= -f2)
        echo "✓ Ответ: ${time}ms"
    elif echo "$line" | grep -q "packet loss"; then
        loss=$(echo "$line" | grep -o "[0-9]*%")
        echo "Потеря пакетов: $loss"
    elif echo "$line" | grep -q "unknown host"; then
        echo "✗ Хост не найден!"
        exit 1
    fi
done
