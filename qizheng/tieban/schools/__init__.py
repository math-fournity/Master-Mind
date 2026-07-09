"""铁板神数学派实现。"""
from .base import TiebanSchool
from .nanpai import NanpaiSchool
from .beipai import BeipaiSchool
from .jiangnan import JiangnanSchool

SCHOOLS = {
    'nanpai': NanpaiSchool,
    'beipai': BeipaiSchool,
    'jiangnan': JiangnanSchool,
}


def get_school(name: str) -> TiebanSchool:
    """获取学派实例。"""
    cls = SCHOOLS.get(name)
    if cls is None:
        raise ValueError(f"未知学派: {name}，可选: {list(SCHOOLS.keys())}")
    return cls()
