from fastapi import FastAPI, Header
from fastapi.middleware.cors import CORSMiddleware

from config import meta_thread_api_token, thread_user_id

app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://localhost:80",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/")
def root() -> dict:
    return {"message" : "ok"}