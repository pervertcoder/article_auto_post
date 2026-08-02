from pydantic import BaseModel

class Request_instagram(BaseModel):
    content: str

class Request_threads(BaseModel):
    content: str

class Response_threads(BaseModel):
    ok: bool