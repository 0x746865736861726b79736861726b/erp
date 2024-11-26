import uuid

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from app.models.base_model import Base


class Products(Base):
    name = Column(String, nullable=False)
    unit = Column(String, nullable=False)
    sku = Column(String, unique=True, nullable=False)
