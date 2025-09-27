from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

# Import your existing API
from api.main import app as api_app

# Create main app
app = FastAPI(title="Doctor's Assistant Chatbot")

# Mount the API
app.mount("/api", api_app)

# Serve static files
@app.get("/")
async def read_index():
    return FileResponse('index.html')

@app.get("/{path:path}")
async def read_static(path: str):
    # Check if it's an API route
    if path.startswith("api/"):
        raise HTTPException(status_code=404, detail="API route not found")
    
    # Serve index.html for all other routes (SPA routing)
    return FileResponse('index.html')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
