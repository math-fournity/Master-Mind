#!/bin/bash
# arango_backup.sh —— [P0-8.4] ArangoDB定期备份脚本
#
# 备份xishujuzhen_math数据库到 /data/master-mind/backups/arango/YYYYMMDD/
# 保留最近14天备份
#
# 使用方式：
#   bash xishujuzhen/arango_backup.sh           # 手动执行
#   crontab: 0 3 * * * bash /data/master-mind/xishujuzhen/arango_backup.sh  # 每天凌晨3点

set -euo pipefail

BACKUP_BASE="/data/master-mind/backups/arango"
DATE=$(date +%Y%m%d)
BACKUP_DIR="${BACKUP_BASE}/${DATE}"
DB_NAME="xishujuzhen_math"
ARANGO_HOST="http://localhost:8529"
RETENTION_DAYS=14

echo "=== ArangoDB备份 ${DATE} ==="
echo "目标: ${BACKUP_DIR}"

# 创建备份目录
mkdir -p "${BACKUP_DIR}"

# 使用arangodump备份数据库
arangodump \
  --server.endpoint "${ARANGO_HOST}" \
  --server.username root \
  --server.password REDACTED-DB-PASSWORD \
  --database "${DB_NAME}" \
  --output-directory "${BACKUP_DIR}" \
  --overwrite true \
  --compress-output true

echo "✅ 备份完成: ${BACKUP_DIR}"

# 清理过期备份
find "${BACKUP_BASE}" -maxdepth 1 -type d -name "20*" -mtime +${RETENTION_DAYS} -exec rm -rf {} \; 2>/dev/null || true
echo "✅ 已清理 ${RETENTION_DAYS} 天前的备份"

# 显示备份列表
echo ""
echo "当前备份列表:"
ls -1d "${BACKUP_BASE}"/20* 2>/dev/null | head -20
