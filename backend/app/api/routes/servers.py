from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.server import ServerCreate, ServerResponse
from app.services.server_service import (
    create_server,
    get_servers,
    get_server,
    delete_server,
)

router = APIRouter(prefix="/servers", tags=["Servers"])


@router.post("/", response_model=ServerResponse)
def create(server: ServerCreate, db: Session = Depends(get_db)):
    return create_server(db, server)


@router.get("/", response_model=list[ServerResponse])
def read_all(db: Session = Depends(get_db)):
    return get_servers(db)


@router.get("/{server_id}", response_model=ServerResponse)
def read_one(server_id: int, db: Session = Depends(get_db)):
    server = get_server(db, server_id)

    if not server:
        raise HTTPException(status_code=404, detail="Server not found")

    return server


@router.delete("/{server_id}")
def remove(server_id: int, db: Session = Depends(get_db)):
    server = delete_server(db, server_id)

    if not server:
        raise HTTPException(status_code=404, detail="Server not found")

    return {"message": "Server deleted successfully"}