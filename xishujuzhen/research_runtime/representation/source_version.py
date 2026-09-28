"""
P7-1.4 表示映射的来源版本和撤稿状态监控——R-15风险防线。

128号§2 R-15：来源许可证/版本漂移。
边界情况：来源无版本信息→告警；来源已撤稿但仍在使用→告警+标记。
"""

from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional
from datetime import datetime


@dataclass
class SourceVersion:
    """来源版本信息。"""
    source_id: str
    title: str
    version: str = ""
    published_date: str = ""
    retracted: bool = False
    retraction_date: str = ""
    license: str = ""

    def to_dict(self) -> dict:
        return {
            "source_id": self.source_id,
            "title": self.title,
            "version": self.version,
            "published_date": self.published_date,
            "retracted": self.retracted,
            "retraction_date": self.retraction_date,
            "license": self.license,
        }


class SourceVersionMonitor:
    """
    P7-1.4：来源版本和撤稿状态监控。

    R-15防线：来源许可证/版本漂移。
    """

    def __init__(self):
        self._sources: Dict[str, SourceVersion] = {}
        self._warnings: List[Dict[str, Any]] = []

    def register_source(self, source: SourceVersion) -> None:
        self._sources[source.source_id] = source

    def check_version(self, source_id: str) -> Dict[str, Any]:
        """
        检查来源版本信息。

        边界情况：来源无版本信息→告警。
        """
        source = self._sources.get(source_id)
        if source is None:
            self._warnings.append({
                "source_id": source_id,
                "type": "not_found",
                "message": f"来源未注册: {source_id}",
            })
            return {"has_version": False, "warning": "来源未注册"}

        if not source.version:
            self._warnings.append({
                "source_id": source_id,
                "type": "no_version",
                "message": f"来源无版本信息: {source.title}",
            })
            return {"has_version": False, "warning": "来源无版本信息"}

        return {"has_version": True, "version": source.version, "source": source.to_dict()}

    def check_retraction(self, source_id: str, in_use: bool = False) -> Dict[str, Any]:
        """
        检查来源是否已撤稿。

        边界情况：来源已撤稿但仍在使用→告警+标记。
        """
        source = self._sources.get(source_id)
        if source is None:
            return {"retracted": False, "warning": "来源未注册"}

        if source.retracted and in_use:
            self._warnings.append({
                "source_id": source_id,
                "type": "retracted_in_use",
                "message": f"来源已撤稿但仍在使用: {source.title}（撤稿日期: {source.retraction_date}）",
            })
            return {
                "retracted": True,
                "in_use": True,
                "warning": "来源已撤稿但仍在使用",
                "retraction_date": source.retraction_date,
            }

        return {"retracted": source.retracted, "in_use": in_use}

    def check_license(self, source_id: str) -> Dict[str, Any]:
        """检查来源许可证。"""
        source = self._sources.get(source_id)
        if source is None:
            return {"has_license": False, "warning": "来源未注册"}
        return {"has_license": bool(source.license), "license": source.license}

    def get_warnings(self) -> List[Dict[str, Any]]:
        return list(self._warnings)

    def check_representation_map_sources(self, rep_map) -> Dict[str, Any]:
        """
        检查RepresentationMap引用的所有来源（evidence字段）。
        """
        results = []
        for ev_id in rep_map.evidence:
            version_check = self.check_version(ev_id)
            retraction_check = self.check_retraction(ev_id, in_use=True)
            license_check = self.check_license(ev_id)
            results.append({
                "source_id": ev_id,
                "version_check": version_check,
                "retraction_check": retraction_check,
                "license_check": license_check,
            })

        all_ok = all(
            r["version_check"].get("has_version", False)
            and not r["retraction_check"].get("retracted", False)
            for r in results
        )

        return {
            "rep_id": rep_map.rep_id,
            "sources_checked": len(results),
            "all_ok": all_ok,
            "results": results,
            "warnings": self.get_warnings(),
        }
