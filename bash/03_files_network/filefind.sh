#!/bin/bash
# Ищет файлы по имени в текущей директории

read -p "Введите часть имени для поиска: " pattern

echo "Ищем файлы с '$pattern'..."
echo "------------------------"

find . -type f -name "*$pattern*" 2>/dev/null | while read file; do
    echo "  ${file#./}"
done

count=$(find . -type f -name "*$pattern*" 2>/dev/null | wc -l)
echo "------------------------"
echo "Найдено файлов: $count"
