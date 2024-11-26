import uuid

from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, ForeignKey, TIMESTAMP

from app.models.base_model import Base


class TaxInvoces(Base):
    tax_invoce_number = Column(String, unique=True, nullable=False)
    tax_invoce_date = Column(TIMESTAMP, nullable=False)
    document_id = Column(UUID(as_uuid=True), ForeignKey("documents.id"), nullable=False)

    document = relationship("Documents", back_populates="tax_invoices")
