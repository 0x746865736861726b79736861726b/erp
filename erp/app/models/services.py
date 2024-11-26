import uuid

from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, String, ForeignKey

from app.models.base_model import Base


class Services(Base):
    name = Column(String, nullable=False)
    code = Column(String, unique=True, nullable=False)
