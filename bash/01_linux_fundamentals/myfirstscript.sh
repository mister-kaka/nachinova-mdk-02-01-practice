#!/bin/bash
# Мой первый скрипт

# 1. дата и время
echo "=== Сейчас ==="
date

# 2. где я нахожусь и что здесь лежит
echo "=== Моя папка ==="
pwd
ls -la

# 3. папка для логов
mkdir -p logs

# 4. пишу данные в лог
echo "Когда: $(date)" > logs/info.log
echo "Кто: $(whoami)" >> logs/info.log
echo "Система: $(uname -a)" >> logs/info.log

# 5. показываю лог
echo "=== Что в логе ==="
cat logs/info.log

# 6. проверяю сеть
echo "=== Есть ли интернет ==="
ping -c 2 8.8.8.8 > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "Интернет есть"
else
    echo "Интернета нет"
fi

# 7. место на диске
echo "=== Место на диске ==="
df -h /home

echo "=== Скрипт закончил работу ==="
