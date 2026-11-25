#!/bin/bash
# Простой счётчик от 1 до N

read -p "До скольки считать? " max

if ! [[ "$max" =~ ^[0-9]+$ ]]; then
    echo "Введите число!"
    exit 1
fi

echo "Считаем от 1 до $max:"

for ((i=1; i<=$max; i++)); do
    echo -n "$i "
    sleep 0.5
done

echo
echo "Готово!"
