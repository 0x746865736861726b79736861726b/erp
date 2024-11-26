import uuid

from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, ForeignKey, TIMESTAMP, CheckConstraint

from app.models.base_model import Base


class Order(Base):
    order_number = Column(String, unique=True, nullable=True)
    order_date = Column(TIMESTAMP, nullable=False)
    client_id = Column(UUID(as_uuid=True), ForeignKey("partners.id"), nullable=False)
    status = Column(
        String,
        nullable=False,
    )
    client = relationship("Partners", back_populates="orders")

    __table_args__ = (
        CheckConstraint("status IN ('new', 'accepted')", name="check_status"),
    )
