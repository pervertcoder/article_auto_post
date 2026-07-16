from fastapi import FastAPI, Header
from fastapi.middleware.cors import CORSMiddleware

from config import meta_thread_api_token, thread_user_id

app = FastAPI()

origins = [
    "http://127.0.0.1:8000",
    "http://127.0.0.1:80",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/health")
def health_check() -> dict:
    return {"message" : "ok"}