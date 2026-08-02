from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from request_response_schema import Request_instagram, Request_threads, Response_threads
from config import meta_thread_api_token, thread_user_id
from data_cleaning import cleaning_data
from meta_api import making_post_container, making_real_text_post

app = FastAPI()

origins = [
    "http://127.0.0.1:3000",
    # production url
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

@app.post("/poster/instagram")
def post_ig(request:Request_instagram) -> dict:
    ...

@app.post("/poster/threads", response_model=Response_threads)
def post_threads(request: Request_threads) -> dict:
    if not request.content: # request is not dict, but an object(Request_threads is a class not dict), that is why it cannot use dict[key_name:str]
        return {"ok": False}
    content = cleaning_data(request.content)
    url_for_container = f"https://graph.threads.com/v1.0/{thread_user_id}/threads"
    url_for_publish = f"https://graph.threads.com/v1.0/{thread_user_id}/threads_publish"
    payload_for_post_container = {
        "media_type": "TEXT",
        "text": content,
        "access_token": meta_thread_api_token
    }

    thread_post_container_id = making_post_container(url_for_container, payload_for_post_container)["container_id"]

    payload_for_real_post = {
        "creation_id": thread_post_container_id,
        "access_token": meta_thread_api_token
    }

    formal_post_id = making_real_text_post(url_for_publish, payload_for_real_post)["thread_media_id"]

    result = {}
    if formal_post_id:
        result["ok"] = True
    else:
        result["ok"] = False
    return result


@app.post("/poster/X")
def post_X() -> dict:
    ...