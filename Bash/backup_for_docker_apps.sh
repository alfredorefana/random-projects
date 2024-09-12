#!/bin/bash

WORK_DIR=/home/pi/zDocker

DEST_DIR='/mnt/hdd/zzzBackups'
TIME_STAMP=$(date -d "today" +"%Y%m%d%H%M%S")

BACKUP_CMD='/bin/tar -cvzf'

cd $WORK_DIR

for app in *; do
        echo "============= Backing up $app ==============="

        DEST_BKP_FILE="$DEST_DIR/$app-$TIME_STAMP.tar.gz"
        sudo $BACKUP_CMD $DEST_BKP_FILE $app/*
        echo 'The generated backup file is: ' $DEST_BKP_FILE

        echo "=============================================="
done

# Deleting old backups
/usr/bin/find $DEST_DIR -mtime +5 -delete
