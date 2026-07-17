from fastapi import FastAPI, Header
from fastapi.middleware.cors import CORSMiddleware

from request_response_schema import Request_instagram
from config import meta_thread_api_token, thread_user_id
from data_cleaning import cleaning_data

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

prefix = "post"

@app.get("/health")
def health_check() -> dict:
    return {"message" : "ok"}

@app.post(f"/{prefix}/instagram")
def post_ig(request:Request_instagram) -> dict:
    ...

@app.post(f"/{prefix}/threads")
def post_threads() -> dict:
    ...


@app.post(f"/{prefix}/X")
def post_X() -> dict:
    ...