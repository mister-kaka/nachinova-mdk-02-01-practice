#!/bin/bash
# Перевод секунд в часы, минуты, секунды

# задание 6: секунды можно передать аргументом
if [ -z "$1" ]; then
    read -p "Введите количество секунд: " total
else
    total=$1
fi

# 3661 секунда = 1 час, 1 минута, 1 секунда
hours=$((total / 3600))            # сколько часов
remainder=$((total % 3600))        # что осталось после часов
minutes=$((remainder / 60))        # сколько минут
seconds=$((remainder % 60))        # что осталось после минут

echo "---"
echo "$total секунд = $hours ч $minutes мин $seconds с"
