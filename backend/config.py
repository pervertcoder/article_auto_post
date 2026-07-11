from dotenv import load_dotenv
import os

load_dotenv()

meta_thread_api_token = os.getenv("META_THREAD_API_TOKEN")
thread_user_id = os.getenv("THREAD_USER_ID")