import requests

from config import thread_user_id, meta_thread_api_token


user_id = thread_user_id
access_token = meta_thread_api_token

url1 = f"https://graph.threads.net/v1.0/{user_id}/threads"
url2 = f"https://graph.threads.net/v1.0/{user_id}/threads_publish"

payload1 = {}
# payload and api format example for url1

# curl -i -X POST \
#   -d "media_type=IMAGE" \
#   -d "image_url=<IMAGE_URL>" \
#   -d "text=<TEXT>" \
#   -d "access_token=<ACCESS_TOKEN>" \
# "https://graph.threads.net/v1.0/<THREADS_USER_ID>/threads"


payload2 = {}
# payload and api format example for url2

# curl -i -X POST \
#   -d "creation_id=<MEDIA_CONTAINER_ID>" \
#   -d "access_token=<ACCESS_TOKEN>" \
# "https://graph.threads.net/v1.0/<THREADS_USER_ID>/threads_publish"


def making_post_container(url:str, payload:dict) -> dict:
    result = {}
    post_container_response = requests.post(url, payload)
    data = post_container_response.json()
    container_id = data["id"]
    if container_id:
        result["state"] = True
        result["container_id"] = container_id
    else:
        result["state"] = False
        result["container_id"] = None

    return result

def making_real_text_post(url:str, payload:dict) -> dict:
    result = {}
    post_response = requests.post(url, payload)
    data = post_response.json()
    thread_media_id = data["id"]
    if thread_media_id:
        result["state"] = True
        result["thread_media_id"] = thread_media_id
    else:
        result["state"] = False
        result["thread_media_id"] = None

    return result