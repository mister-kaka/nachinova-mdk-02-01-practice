#!/bin/bash
echo "grep: поиск строки"
grep mariia /etc/passwd

echo "awk: третье поле этой строки"
grep mariia /etc/passwd | awk -F: '{print $1, $3}'

echo "sed: замена текста"
echo "студент Мария" | sed 's/Мария/Начинова/'

echo "find: поиск файлов"
find /home/mariia_nachinova/lab/pr1 -name "*.sh"

echo "curl: заголовок страницы"
curl -I -s https://example.com | head -n 5

echo "wget: скачать страницу в файл"
wget -q -O страница.txt https://example.com
ls -l страница.txt
