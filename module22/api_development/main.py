import uvicorn
from module22.api_development import app

if __name__ == "__main__":
    uvicorn.run(app, host=" http://127.0.0.1:8000", port=8000)