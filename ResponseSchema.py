from pydantic import BaseModel


class StatusResponse(BaseModel):
    status: str
    message: str | None = None
    class Config:
        arbitrary_types_allowed = True

class TokenResponse(BaseModel):
    access_token:str
    token_type: str