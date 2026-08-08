#!/usr/bin/env bash
# backup_arango.sh —— ArangoDB 定期备份脚本
#
# ArangoDB 跑在 Docker 容器 arangodb 中，arangodump 在容器内。
# 本脚本通过 docker exec 在容器内执行 arangodump，再 docker cp 到宿主机。
#
# 用法：
#   ./scripts/backup_arango.sh              # 备份本 repo 数据库（xishujuzhen_math_glm52）
#   ./scripts/backup_arango.sh --db <name>  # 备份指定数据库
#   ./scripts/backup_arango.sh --keep 7     # 保留最近 7 天（默认）
#   ./scripts/backup_arango.sh --dry-run    # 只打印命令不执行
#
# cron 定时示例（每天凌晨 3 点）：
#   0 3 * * * /data/master-mind-glm5.2-grove/scripts/backup_arango.sh >> /data/master-mind/backups/arango/backup.log 2>&1

set -euo pipefail

# 默认参数
DB_NAME="xishujuzhen_math_glm52"
ARANGO_USER="root"
ARANGO_PASS="REDACTED-DB-PASSWORD"
KEEP_DAYS=7
DRY_RUN=0
CONTAINER="arangodb"
BACKUP_ROOT="/data/master-mind/backups/arango"

# 解析参数
while [[ $# -gt 0 ]]; do
    case "$1" in
        --db) DB_NAME="$2"; shift 2 ;;
        --keep) KEEP_DAYS="$2"; shift 2 ;;
        --dry-run) DRY_RUN=1; shift ;;
        *) echo "未知参数: $1"; exit 1 ;;
    esac
done

DATE=$(date +%Y%m%d)
BACKUP_DIR="${BACKUP_ROOT}/${DATE}"
CONTAINER_TMP="/tmp/arango-backup-${DATE}"

echo "=========================================="
echo "ArangoDB 备份"
echo "  数据库: ${DB_NAME}"
echo "  日期: ${DATE}"
echo "  备份到: ${BACKUP_DIR}"
echo "  保留天数: ${KEEP_DAYS}"
echo "  dry-run: ${DRY_RUN}"
echo "=========================================="

# 检查容器运行状态
if ! docker ps --format '{{.Names}}' | grep -q "^${CONTAINER}$"; then
    echo "❌ Docker 容器 ${CONTAINER} 未运行"
    exit 1
fi

# 执行备份
if [[ ${DRY_RUN} -eq 1 ]]; then
    echo "[dry-run] docker exec ${CONTAINER} arangodump"
    echo "  --server.endpoint tcp://127.0.0.1:8529"
    echo "  --server.database ${DB_NAME}"
    echo "  --server.username ${ARANGO_USER}"
    echo "  --server.password ***"
    echo "  --output-directory ${CONTAINER_TMP}"
    echo "[dry-run] docker cp ${CONTAINER}:${CONTAINER_TMP} ${BACKUP_DIR}"
    echo "[dry-run] docker exec ${CONTAINER} rm -rf ${CONTAINER_TMP}"
    echo "[dry-run] find ${BACKUP_ROOT} -maxdepth 1 -type d -mtime +${KEEP_DAYS} -exec rm -rf {} +"
    exit 0
fi

# 1. 容器内 arangodump
echo "▶ 容器内 arangodump..."
docker exec "${CONTAINER}" arangodump \
    --server.endpoint tcp://127.0.0.1:8529 \
    --server.database "${DB_NAME}" \
    --server.username "${ARANGO_USER}" \
    --server.password "${ARANGO_PASS}" \
    --output-directory "${CONTAINER_TMP}" \
    --overwrite true

# 2. 从容器复制到宿主机
echo "▶ docker cp 到宿主机..."
mkdir -p "${BACKUP_DIR}"
docker cp "${CONTAINER}:${CONTAINER_TMP}/." "${BACKUP_DIR}/"

# 3. 清理容器内临时目录
echo "▶ 清理容器内临时目录..."
docker exec "${CONTAINER}" rm -rf "${CONTAINER_TMP}"

# 4. 清理过期备份
echo "▶ 清理 ${KEEP_DAYS} 天前的备份..."
find "${BACKUP_ROOT}" -maxdepth 1 -type d -name "20*" -mtime +${KEEP_DAYS} -exec rm -rf {} + 2>/dev/null || true

# 5. 验证
echo ""
echo "=========================================="
echo "备份完成"
echo "=========================================="
echo "备份目录: ${BACKUP_DIR}"
echo "文件列表:"
ls -lh "${BACKUP_DIR}/" | head -20
echo ""
echo "现有备份:"
ls -1 "${BACKUP_ROOT}" | grep "^20" || echo "  (无)"
echo ""
echo "备份大小:"
du -sh "${BACKUP_DIR}"
