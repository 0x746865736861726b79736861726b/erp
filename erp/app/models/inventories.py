import uuid

from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, ForeignKey, TIMESTAMP, Numeric

from app.models.base_model import Base


class Inventory(Base):
    product_id = Column(UUID(as_uuid=True), ForeignKey("products.id"), nullable=False)
    batch_number = Column(String, nullable=False)
    entry_date = Column(TIMESTAMP, nullable=False)
    quantity = Column(Numeric, nullable=False)
    cost = Column(Numeric, nullable=False)

    product = relationship("Products", back_populates="inventory")
