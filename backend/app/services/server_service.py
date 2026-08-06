from sqlalchemy.orm import Session

from app.models.server import Server
from app.schemas.server import ServerCreate


def create_server(db: Session, server: ServerCreate):
    db_server = Server(
        name=server.name,
        ip_address=server.ip_address,
        status=server.status
    )

    db.add(db_server)
    db.commit()
    db.refresh(db_server)

    return db_server


def get_servers(db: Session):
    return db.query(Server).all()


def get_server(db: Session, server_id: int):
    return db.query(Server).filter(Server.id == server_id).first()


def delete_server(db: Session, server_id: int):
    server = db.query(Server).filter(Server.id == server_id).first()

    if server:
        db.delete(server)
        db.commit()

    return server