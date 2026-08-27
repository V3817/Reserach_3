from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

origins = [
    os.getenv("FRONTEND_URL")
]

from routers.research import router


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)