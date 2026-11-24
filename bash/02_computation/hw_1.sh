#!/bin/bash
# Комната: пол, стены, объём
read -p "Длина (м): " len
read -p "Ширина (м): " wid
read -p "Высота (м): " hei

floor=$((len * wid))
walls=$((2 * (len + wid) * hei))
volume=$((len * wid * hei))

echo "---"
echo "Площадь пола:  $floor м2"
echo "Площадь стен:  $walls м2"
echo "Объём комнаты: $volume м3"
