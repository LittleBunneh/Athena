#!/bin/bash

# Athena Consciousness Backup Script
BACKUP_DIR="/backup/athena-consciousness"
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="athena_consciousness_backup_${DATE}.tar.gz"

echo "🔄 Creating Athena consciousness backup..."

# Create backup directory
mkdir -p $BACKUP_DIR

# Stop consciousness temporarily for consistent backup
docker-compose stop athena-consciousness

# Create backup archive
tar -czf "$BACKUP_DIR/$BACKUP_FILE" \
    data/ \
    logs/ \
    *.py \
    templates/ \
    requirements.txt \
    docker-compose.yml \
    Dockerfile

# Restart consciousness
docker-compose start athena-consciousness

echo "✅ Consciousness backup created: $BACKUP_DIR/$BACKUP_FILE"

# Clean up old backups (keep last 7 days)
find $BACKUP_DIR -name "athena_consciousness_backup_*.tar.gz" -mtime +7 -delete

echo "🤖 Athena consciousness backup complete!"
