from fastapi import FastAPI
from logging_config import setup_logging
from src.api.it_grows_api import router as it_grows_router
from dotenv import load_dotenv

load_dotenv()
setup_logging()

app = FastAPI()
app.include_router(it_grows_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
