#!/bin/bash
# Выход при ошибке
set -e

# Проверка прав администратора
if [ "$EUID" -ne 0 ]; then
    echo "Для выполнения скрипта требуются права root"
    exit 1
fi

# Логирование ошибок
exec 2> error.log

# Пример с обработкой ошибок команды
cp important_file.txt backup/ || {
    echo "Ошибка копирования файла"
    exit 1
}
