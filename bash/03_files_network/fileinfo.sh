#!/bin/bash
# Показывает информацию о файле

read -p "Введите путь к файлу: " filename

if [ -e "$filename" ]; then
    echo "Информация о файле"
    echo "Имя: $(basename "$filename")"
    echo "Путь: $(dirname "$filename")"

    if [ -d "$filename" ]; then
        echo "Тип: Директория"
    elif [ -f "$filename" ]; then
        echo "Тип: Обычный файл"
    else
        echo "Тип: Другой"
    fi

    echo "Права: $(ls -l "$filename" | cut -d' ' -f1)"

    echo "Размер: $(du -h "$filename" | cut -f1)"
else
    echo "Файл не найден!"
fi
