"""
Vercel serverless function handler for FastAPI
This file is required for Vercel to properly handle FastAPI routes
"""
import sys
import os

# Add backend directory to path
backend_path = os.path.join(os.path.dirname(__file__), '..', 'backend')
sys.path.insert(0, backend_path)

try:
    from app.main import app
    handler = app
except Exception as e:
    # Create a minimal error handler if import fails
    from fastapi import FastAPI, HTTPException
    error_app = FastAPI()
    
    @error_app.get("/{path:path}")
    async def error_handler(path: str):
        raise HTTPException(
            status_code=500,
            detail=f"Failed to initialize app: {str(e)}. Please check environment variables and logs."
        )
    
    handler = error_app

