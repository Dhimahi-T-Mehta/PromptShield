from dotenv import load_dotenv

load_dotenv()
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router
from app.api import chat_routes
from app.auth.auth_routes import router as auth_router

from app.api.admin_routes import router as admin_router

app = FastAPI(
    title="PromptShield",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    router,
    prefix="/api/v1"
)


app.include_router(
    chat_routes.router,
    prefix="/api/v1"
)

app.include_router(
    admin_router,
    prefix="/api/v1",
)

app.include_router(auth_router)

@app.get("/")
def root():

    return {
        "status": "running",
        "project": "PromptShield"
    }