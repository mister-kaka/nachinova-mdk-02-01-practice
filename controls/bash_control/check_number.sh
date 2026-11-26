#!/bin/bash
# проверка числа
num="$1"

if [ -z "$num" ]; then
    echo "Ошибка: не указано число. Пример: ./check_number.sh 7"
    exit 1
fi

if ! [[ "$num" =~ ^-?[0-9]+$ ]]; then
    echo "Ошибка: \"$num\" не является целым числом"
    exit 1
fi

if [ "$num" -gt 0 ]; then
    echo "Число $num является положительным"
elif [ "$num" -lt 0 ]; then
    echo "Число $num является отрицательным"
else
    echo "Число $num является нулём"
fi
