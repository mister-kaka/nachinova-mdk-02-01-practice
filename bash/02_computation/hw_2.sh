#!/bin/bash
# Доход по вкладу за 1 год
read -p "Сумма вклада: " deposit
read -p "Процентная ставка (%): " rate

profit=$((deposit * rate / 100))
echo "---"
echo "Доход за 1 год: $profit руб."
echo "Итого на счёте: $((deposit + profit)) руб."
