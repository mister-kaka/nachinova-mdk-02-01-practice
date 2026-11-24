#!/bin/bash
# Дробные вычисления через bc

read -p "Радиус: " r

# Площадь круга = π × r²
area=$(echo "scale=2; 3.14159 * $r * $r" | bc)

echo "---"
echo "Радиус: $r"
echo "Площадь круга: $area"
