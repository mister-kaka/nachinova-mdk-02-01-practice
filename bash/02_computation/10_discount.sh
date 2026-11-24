#!/bin/bash
# Расчёт цены со скидкой

read -p "Цена товара: " price
read -p "Скидка (%): " discount

# Считаем скидку
discount_amount=$((price * discount / 100))
final_price=$((price - discount_amount))

# задание 5: предупреждение при скидке больше 50%
if [ "$discount" -gt 50 ]; then
    echo "Внимание: скидка больше 50%!"
fi

echo "---"
echo "Исходная цена: $price руб."
echo "Скидка $discount%: $discount_amount руб."
echo "Итого к оплате: $final_price руб."
