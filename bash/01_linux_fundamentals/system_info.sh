#!/bin/bash
# Сложное задание: сведения о системе
echo "Имя хоста:        $(hostname)"
echo "Версия ядра:      $(uname -r)"
echo "Свободная память: $(free -h | awk '/Mem/ {print $4}')"
echo "Текущий пользователь: $(whoami)"
echo "Время работы:     $(uptime -p)"
echo "Запущенные процессы (первые 10):"
ps aux | head -10
