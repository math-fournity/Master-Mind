"""
系统日志——滚动日志到system/logs/

特性：
- 单文件不超过1MB，超过自动滚动到新文件
- 整个目录不超过500MB（500个文件 × 1MB）
- 日志文件名：vein_analysis.log（当前）+ vein_analysis.log.N（滚动备份）
- 格式：[timestamp] [level] [module] message
- 同时输出到stdout（INFO级别以上）

用法：
    from system.log import get_logger
    logger = get_logger("vein_analysis")
    logger.info("三阶段脉络分析启动")
    logger.warning("版本V7超时")
    logger.error("所有版本失败")
"""

import logging
import os
from logging.handlers import RotatingFileHandler

_LOG_DIR: str = ""


def _get_log_dir() -> str:
    """获取日志目录路径（惰性计算）"""
    global _LOG_DIR
    if not _LOG_DIR:
        repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        _LOG_DIR = os.path.join(repo_root, "system", "logs")
    return _LOG_DIR


def get_logger(name: str = "vein_analysis") -> logging.Logger:
    """获取日志logger

    Args:
        name: logger名称（模块名）

    Returns:
        logging.Logger实例
    """
    log_dir = _get_log_dir()
    os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger(name)
    if logger.handlers:
        return logger  # 避免重复添加handler

    logger.setLevel(logging.DEBUG)

    # 滚动文件handler——单文件1MB，最多500个备份（500MB）
    log_file = os.path.join(log_dir, "vein_analysis.log")
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=1 * 1024 * 1024,  # 1MB
        backupCount=500,            # 500个备份 × 1MB = 500MB
        encoding="utf-8",
    )
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # 同时输出到stdout（INFO级别以上）
    stdout_handler = logging.StreamHandler()
    stdout_handler.setLevel(logging.INFO)
    stdout_handler.setFormatter(formatter)
    logger.addHandler(stdout_handler)

    return logger
