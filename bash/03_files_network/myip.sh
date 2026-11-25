#!/bin/bash
# Показывает IP адреса компьютера

echo "Внутренние IP адреса"
ip addr | grep inet | grep -v inet6 | while read line; do
    ip=$(echo "$line" | awk '{print $2}' | cut -d'/' -f1)
    if [ "$ip" != "127.0.0.1" ]; then
        echo "  $ip"
    fi
done

echo
echo "Внешний IP (через интернет)"
curl -s ifconfig.me
echo
