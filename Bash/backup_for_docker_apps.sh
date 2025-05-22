#!/bin/bash

WORK_DIR='/root/apps'

DEST_DIR='/mnt/nas/backups/docker/'
TIME_STAMP=$(date -d "today" +"%Y%m%d%H%M%S")

BACKUP_CMD='/bin/tar -cvzf'

cd $WORK_DIR

for app in *; do
        echo "============= Backing up $app ==============="

        DEST_BKP_FILE="$DEST_DIR/$app-$TIME_STAMP.tar.gz"
        $BACKUP_CMD $DEST_BKP_FILE $app/.
        echo 'The generated backup file is: ' $DEST_BKP_FILE

        echo "=============================================="
done

# Deleting old backups
/usr/bin/find $DEST_DIR -mtime +5 -delete
