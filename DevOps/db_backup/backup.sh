#!/bin/bash

# Database credentials
DB_NAME="your_database_name"
DB_USER="your_database_user"
DB_PASSWORD="your_database_password"

# Backup directory
BACKUP_DIRECTORY="/path/to/backup/directory"

# Google Drive directory ID (replace with your actual Google Drive directory ID)
GOOGLE_DRIVE_DIR_ID="18rH4XsYsDJUWCeSEya6H6adiCsGkeNvk?q=parent:18rH4XsYsDJUWCeSEya6H6adiCsGkeNvk"

# Date format for the backup files
DATE=$(date +"%Y%m%d%H%M%S")

# Create backup filenames
DJANGO_BACKUP_FILE="${BACKUP_DIRECTORY}/${DB_NAME}_django_backup_${DATE}.json"
MYSQL_BACKUP_FILE="${BACKUP_DIRECTORY}/${DB_NAME}_mysql_backup_${DATE}.sql"

# Backup the Django database using dumpdata
python manage.py dumpdata > "${DJANGO_BACKUP_FILE}"

# Check if Django dumpdata was successful
if [ $? -eq 0 ]; then
    echo "Django database backup created successfully: ${DJANGO_BACKUP_FILE}"
else
    echo "Error creating Django database backup"
    exit 1
fi

# Use mysqldump to create MySQL database backup
mysqldump -u "${DB_USER}" -p"${DB_PASSWORD}" "${DB_NAME}" > "${MYSQL_BACKUP_FILE}"

# Check if mysqldump was successful
if [ $? -eq 0 ]; then
    echo "MySQL database backup created successfully: ${MYSQL_BACKUP_FILE}"
else
    echo "Error creating MySQL database backup"
    exit 1
fi

# Upload backup files to Google Drive
# Make sure you have 'gdrive' command-line tool installed and authenticated
gdrive upload --parent "${GOOGLE_DRIVE_DIR_ID}" "${DJANGO_BACKUP_FILE}"
gdrive upload --parent "${GOOGLE_DRIVE_DIR_ID}" "${MYSQL_BACKUP_FILE}"

# Check if uploads were successful
if [ $? -eq 0 ]; then
    echo "Backups uploaded to Google Drive"
else
    echo "Error uploading backups to Google Drive"
fi
