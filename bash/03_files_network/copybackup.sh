#!/bin/bash
# Копирует файл с созданием бэкапа

read -p "Файл для копирования: " source
read -p "Куда копировать: " dest

if [ ! -f "$source" ]; then
    echo "Ошибка: Файл $source не найден!"
    exit 1
fi

if [ -f "$dest" ]; then
    backup="${dest}.backup.$(date +%Y%m%d_%H%M%S)"
    cp "$dest" "$backup"
    echo "Создан бэкап: $backup"
fi

cp "$source" "$dest"
echo "Файл скопирован в: $dest"
