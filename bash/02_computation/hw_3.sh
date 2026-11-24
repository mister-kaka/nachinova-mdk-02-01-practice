#!/bin/bash
# Чётность и делимость
read -p "Введите число N: " nn

if [ $((nn % 2)) -eq 0 ]; then
    echo "$nn - чётное"
else
    echo "$nn - нечётное"
fi

if [ $((nn % 3)) -eq 0 ]; then
    echo "$nn делится на 3"
else
    echo "$nn не делится на 3"
fi

if [ $((nn % 5)) -eq 0 ]; then
    echo "$nn делится на 5"
else
    echo "$nn не делится на 5"
fi
