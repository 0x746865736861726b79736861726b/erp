import uuid

from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, ForeignKey, TIMESTAMP, Numeric

from app.models.base_model import Base


class Invoice(Base):
    order_id = Column(UUID(as_uuid=True), ForeignKey("orders.id"), nullable=False)
    invoice_number = Column(String, unique=True, nullable=False)
    invoice_date = Column(TIMESTAMP, nullable=False)
    total = Column(Numeric, nullable=False)

    order = relationship("Orders", backref="invoices")
