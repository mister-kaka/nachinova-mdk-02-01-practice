#!/bin/bash
# Создаёт файлы с разным содержимым

echo "Что создать?"
echo "1) Пустой файл"
echo "2) Файл с текстом"
echo "3) Файл с датой"
read -p "Выберите (1-3): " choice

case $choice in
    1)
        read -p "Имя файла: " filename
        touch "$filename"
        echo "Создан пустой файл: $filename"
        ;;
    2)
        read -p "Имя файла: " filename
        read -p "Текст для записи: " text
        echo "$text" > "$filename"
        echo "Файл создан с текстом"
        ;;
    3)
        read -p "Имя файла: " filename
        date > "$filename"
        echo "Файл создан с текущей датой"
        cat "$filename"
        ;;
    *)
        echo "Неверный выбор"
        ;;
esac
