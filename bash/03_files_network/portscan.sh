#!/bin/bash
# Проверяет открытые порты на локальной машине

echo "Открытые TCP порты"
ss -tln | grep LISTEN | grep -v 127.0.0.1 | while read line; do
    port=$(echo "$line" | awk '{print $4}' | rev | cut -d: -f1 | rev)
    service=$(getent services "$port" 2>/dev/null | cut -d' ' -f1)
    if [ -n "$service" ]; then
        echo "  Порт $port ($service)"
    else
        echo "  Порт $port"
    fi
done

echo
echo "Открытые UDP порты"
ss -uln | grep UNCONN | grep -v 127.0.0.1 | while read line; do
    port=$(echo "$line" | awk '{print $5}' | rev | cut -d: -f1 | rev)
    service=$(getent services "$port" 2>/dev/null | cut -d' ' -f1)
    if [ -n "$service" ]; then
        echo "  Порт $port ($service)"
    else
        echo "  Порт $port"
    fi
done
