from pydantic import BaseModel


class ServerCreate(BaseModel):
    name: str
    ip_address: str
    status: str = "unknown"


class ServerResponse(BaseModel):
    id: int
    name: str
    ip_address: str
    status: str

    class Config:
        from_attributes = True