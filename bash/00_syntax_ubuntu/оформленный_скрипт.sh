#!/bin/bash
#
# Скрипт для создания резервных копий
# Автор: Начинова М. Д.
# Дата: 10.10.2026

set -euo pipefail

readonly BACKUP_DIR="/var/backups"
readonly SOURCE_DIRS=("/home/mariia_nachinova/documents" "/etc/hostname")
readonly DATE=$(date +%Y%m%d_%H%M%S)

main() {
    check_privileges
    create_backup_dir
    perform_backup
    cleanup_old_backups
}

check_privileges() {
    if [[ $EUID -ne 0 ]]; then
        echo "Ошибка: Скрипт должен запускаться с правами root" >&2
        exit 1
    fi
}

create_backup_dir() {
    if [[ ! -d "$BACKUP_DIR" ]]; then
        mkdir -p "$BACKUP_DIR"
    fi
}

perform_backup() {
    local backup_file="$BACKUP_DIR/backup_$DATE.tar.gz"

    if tar -czf "$backup_file" "${SOURCE_DIRS[@]}" 2>/dev/null; then
        echo "Резервная копия создана: $backup_file"
    else
        echo "Ошибка создания резервной копии" >&2
        exit 1
    fi
}

cleanup_old_backups() {
    find "$BACKUP_DIR" -name "backup_*.tar.gz" -mtime +7 -delete
}

main "$@"
