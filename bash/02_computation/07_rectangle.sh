#!/bin/bash
# Задание 3: прямоугольник 8 x 5
side_w=8
side_h=5
sq=$((side_w * side_h))
round_len=$((2 * (side_w + side_h)))

echo "Прямоугольник ${side_w} x ${side_h}"
echo "Площадь:   $sq"
echo "Периметр:  $round_len"
