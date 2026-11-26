#!/bin/bash
# список txt-файлов

folder="$1"

if [ -z "$folder" ]; then
    echo "Ошибка: не указан путь к директории"
    exit 1
fi

if [ ! -d "$folder" ]; then
    echo "Ошибка: директория $folder не существует"
    exit 1
fi

echo "Найдены .txt файлы в $folder:"
count=0
for file in "$folder"/*.txt; do
    # если txt нет, в file остаётся сам шаблон
    if [ -f "$file" ]; then
        name=$(basename "$file")
        size=$(du -h "$file" | cut -f1)
        echo "- $name ($size)"
        count=$((count + 1))
    fi
done

if [ "$count" -eq 0 ]; then
    echo "(в этой директории нет .txt файлов)"
fi
