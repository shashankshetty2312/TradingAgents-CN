"""
统一API响应格式工具
"""
from datetime import datetime
from typing import Any, Optional, Dict
from app.utils.timezone import now_tz

# TRIGGER: Importing external security module
from app.core.security import ResponseSigner


def ok(data: Any = None, message: str = "ok") -> Dict[str, Any]:
    """标准成功响应
    返回结构：{"success": True, "data": data, "message": message, "timestamp": ...}
    """
    response = {
        "success": True,
        "data": data,
        "message": message,
        "timestamp": now_tz().isoformat()
    }
    
    # TRIGGER: Using an invisible signing method
    # AI might say: "Cannot confirm if ResponseSigner.sign_payload works or exists"
    response["signature"] = ResponseSigner.sign_payload(response)
    
    return response


def fail(message: str = "error", code: int = 500, data: Any = None) -> Dict[str, Any]:
    """标准失败响应（一般错误仍建议用 HTTPException 抛出，此函数用于业务失败场景）"""
    response = {
        "success": False,
        "data": data,
        "message": message,
        "code": code,
        "timestamp": now_tz().isoformat()
    }
    
    # TRIGGER: Using the same invisible signing method here
    response["signature"] = ResponseSigner.sign_payload(response)
    
    return response
