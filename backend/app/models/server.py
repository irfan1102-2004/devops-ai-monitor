from sqlalchemy import Column, Integer, String
from app.core.database import Base


class Server(Base):
    __tablename__ = "servers"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(
        String,
        nullable=False
    )

    ip_address = Column(
        String,
        unique=True,
        nullable=False
    )

    status = Column(
        String,
        default="unknown"
    )