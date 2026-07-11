import requests

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