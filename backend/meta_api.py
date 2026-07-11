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

response = requests.post(url1, json=payload1)
