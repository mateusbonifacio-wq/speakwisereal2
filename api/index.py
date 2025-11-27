"""
Vercel serverless function handler for FastAPI
This file is required for Vercel to properly handle FastAPI routes
"""
import sys
import os

# Add backend directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

from app.main import app

# Vercel expects a handler function
handler = app

