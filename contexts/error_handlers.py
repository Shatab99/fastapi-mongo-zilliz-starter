from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

def setup_global_error_handlers(app: FastAPI):
    
    # 1. Catch standard HTTP Exceptions (e.g., your 400s, 401s, 404s)
    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request: Request, exc: StarletteHTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "success": False, 
                "error": exc.detail
            },
        )

    # 2. Catch Pydantic Validation Errors (422s)
    # FastAPI's default 422 errors are very verbose. This cleans them up into a nice format.
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        # Format the errors to be cleaner for the frontend
        formatted_errors = [{"field": err.get("loc")[-1], "message": err.get("msg")} for err in exc.errors()]
        return JSONResponse(
            status_code=422,
            content={
                "success": False, 
                "error": "Validation Failed", 
                "details": formatted_errors
            },
        )

    # 3. The true "Express-style" catch-all for 500 Internal Server Errors
    # If anything completely breaks your code, it falls down to this handler.
    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        # In production, you would log this to a file or monitoring service (like Sentry)
        print(f"CRITICAL ERROR: {exc}") 
        
        return JSONResponse(
            status_code=500,
            content={
                "success": False, 
                "error": "Internal Server Error",
                # Note: You might want to hide str(exc) in production so you don't leak backend details
                "message": str(exc) 
            },
        )