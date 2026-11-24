#!/bin/bash
echo "Начало обновления системы: $(date)"

# Для Ubuntu
sudo apt update && sudo apt upgrade -y

echo "Обновление завершено: $(date)"
