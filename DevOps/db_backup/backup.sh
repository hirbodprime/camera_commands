#!/bin/bash

MANAGE_PY_DIR='/home/hirbod/makovision/camera_commands'
cd $MANAGE_PY_DIR
# Database credentials
<<<<<<< HEAD
DB_NAME="bash_backup_db"
DB_USER="bash_user1"
DB_PASSWORD="@Bash_pass_12345"

# Backup directory
BACKUP_DIRECTORY="/home/hirbod/makovision/backup_data"
=======
DB_NAME="MKVDB"
DB_USER="hir"
DB_PASSWORD="hirbodaflaki"
DJANGO_PROJECT_DIR="D:/makovision/camera-commands/camera_commands"

# Backup directory
BACKUP_DIRECTORY="D:/makovision/camera-commands/camera_commands/DevOps/db_backup/"

>>>>>>> a647308a936af66c6504e524753ef87f3cc508b8
# Google Drive directory ID (replace with your actual Google Drive directory ID)
GOOGLE_DRIVE_DIR_ID="18rH4XsYsDJUWCeSEya6H6adiCsGkeNvk"

# Date format for the backup files
DATE=$(date +"%Y%m%d%H%M%S")

# Create backup filenames
DJANGO_BACKUP_FILE="${BACKUP_DIRECTORY}/${DB_NAME}_django_backup_${DATE}.json"
MYSQL_BACKUP_FILE="${BACKUP_DIRECTORY}/${DB_NAME}_mysql_backup_${DATE}.sql"
echo $DJANGO_BACKUP_FILE
echo $MYSQL_BACKUP_FILE
# Backup the Django database using dumpdata
python "${DJANGO_PROJECT_DIR}/manage.py" dumpdata > "${DJANGO_BACKUP_FILE}"


# Check if Django dumpdata was successful
if [ $? -eq 0 ]; then
    echo "Django database backup created successfully: ${DJANGO_BACKUP_FILE}"
else
    echo "Error creating Django database backup"
    exit 1
fi

# Use mysqldump to create MySQL database backup
mysqldump -u "${DB_USER}" -p"${DB_PASSWORD}" --skip-events --skip-routines "${DB_NAME}" > "${MYSQL_BACKUP_FILE}"

# Check if mysqldump was successful
if [ $? -eq 0 ]; then
    echo "MySQL database backup created successfully: ${MYSQL_BACKUP_FILE}"
else
    echo "Error creating MySQL database backup"
    exit 1
fi

# Upload backup files to Google Drive
# Make sure you have 'gdrive' command-line tool installed and authenticated
<<<<<<< HEAD
/usr/local/bin/gdrive upload --parent "${GOOGLE_DRIVE_DIR_ID}" "${DJANGO_BACKUP_FILE}"
/usr/local/bin/gdrive upload --parent "${GOOGLE_DRIVE_DIR_ID}" "${MYSQL_BACKUP_FILE}"
=======
# Use absolute path to gdrive executable within the virtual environment
GDRIVE_EXECUTABLE="D:/makovision/camera-commands/myvenv/Lib/site-packages/gdrive/executable"
$GDRIVE_EXECUTABLE upload --parent "${GOOGLE_DRIVE_DIR_ID}" "${DJANGO_BACKUP_FILE}"
$GDRIVE_EXECUTABLE upload --parent "${GOOGLE_DRIVE_DIR_ID}" "${MYSQL_BACKUP_FILE}"

>>>>>>> a647308a936af66c6504e524753ef87f3cc508b8

# Check if uploads were successful
if [ $? -eq 0 ]; then
    echo "Backups uploaded to Google Drive"
else
    echo "Error uploading backups to Google Drive"
fi