"""七政四余推命系统 Web API。

基于 FastAPI 的 RESTful API，封装 build_chart/render_chart/export_json。

启动:
    python -m qizheng.api
    # 或
    uvicorn qizheng.api:app --host 0.0.0.0 --port 8000

接口:
    GET  /              — 服务信息
    GET  /health        — 健康检查
    POST /chart         — 构建命盘（JSON输入→JSON输出）
    POST /chart/text    — 构建命盘（JSON输入→文本输出）
    GET  /chart         — 构建命盘（查询参数→JSON输出）
"""
from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

from qizheng.chart import build_chart
from qizheng.render import render_chart, export_json

app = FastAPI(
    title="七政四余推命系统 API",
    description="排盘/神煞/格局/八字/限运/流年 全功能 RESTful API",
    version="1.0",
)


class ChartRequest(BaseModel):
    year: int = Field(..., description="出生年（公历）", examples=[1990])
    month: int = Field(..., description="出生月（公历，1-12）", examples=[5])
    day: int = Field(..., description="出生日（公历）", examples=[15])
    hour: float = Field(..., description="出生时间（UT小时，如3.5=3:30）", examples=[3.5])
    longitude: float = Field(..., description="地理经度（东经为正）", examples=[116.4])
    latitude: float = Field(..., description="地理纬度（北纬为正）", examples=[39.9])
    verbose: bool = Field(False, description="神煞明细（仅文本模式）")


@app.get("/")
async def root():
    return {
        "service": "七政四余推命系统 API",
        "version": "1.0",
        "endpoints": {
            "POST /chart": "构建命盘（JSON→JSON）",
            "POST /chart/text": "构建命盘（JSON→文本）",
            "GET /chart": "构建命盘（查询参数→JSON）",
            "GET /health": "健康检查",
            "GET /docs": "API文档（Swagger UI）",
        },
    }


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/chart")
async def create_chart(req: ChartRequest):
    """构建命盘，返回 JSON 格式。"""
    try:
        chart = build_chart(
            req.year, req.month, req.day, req.hour,
            req.longitude, req.latitude,
        )
        import json
        j = export_json(chart, pretty=False)
        return json.loads(j)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/chart/text")
async def create_chart_text(req: ChartRequest):
    """构建命盘，返回纯文本格式。"""
    try:
        chart = build_chart(
            req.year, req.month, req.day, req.hour,
            req.longitude, req.latitude,
        )
        text = render_chart(chart, verbose=req.verbose)
        return {"text": text}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/chart")
async def get_chart(
    year: int = Query(..., description="出生年"),
    month: int = Query(..., description="出生月"),
    day: int = Query(..., description="出生日"),
    hour: float = Query(..., description="出生时间（UT小时）"),
    longitude: float = Query(..., description="经度"),
    latitude: float = Query(..., description="纬度"),
):
    """构建命盘（GET 方式，查询参数），返回 JSON 格式。"""
    try:
        chart = build_chart(year, month, day, hour, longitude, latitude)
        import json
        j = export_json(chart, pretty=False)
        return json.loads(j)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
