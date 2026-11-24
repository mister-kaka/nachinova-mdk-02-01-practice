#!/bin/bash
# Игра: угадай число
secret=7
read -p "Угадай число от 1 до 10: " guess

if [ "$guess" -eq "$secret" ]; then
    echo "Победа!"
else
    echo "Не угадал, было $secret"
fi
