#!/bin/bash
# приветствие
read -p "Введите ваше ФИО_ГРУППА: " name

if [ -z "$name" ]; then
    echo "Ошибка: вы ничего не ввели"
    exit 1
fi

echo "Привет, $name! Добро пожаловать в мир Bash!"
