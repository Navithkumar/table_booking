from typing import Any, Optional
from fastapi.responses import JSONResponse


def success_response(
    message: str,
    data: Optional[Any] = None,
    status_code: int = 200,
):
    return JSONResponse(
        status_code=status_code,
        content={
            "is_v1": True,
            "status": "success",
            "message": message,
            "data": data,
        },
    )


def error_response(
    message: str,
    errors: Optional[Any] = None,
    status_code: int = 400,
):
    return JSONResponse(
        status_code=status_code,
        content={
            "is_v1": True,
            "status": "error",
            "message": message,
            "errors": errors,
        },
    )
