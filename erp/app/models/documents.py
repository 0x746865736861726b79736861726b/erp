import uuid

from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, ForeignKey, TIMESTAMP

from app.models.base_model import Base


class Documents(Base):
    doc_type = Column(String, primary_key=True, autoincrement=False)
    doc_number = Column(String, unique=True, nullable=False)
    doc_date = Column(TIMESTAMP, nullable=False)
    partner_id = Column(UUID(as_uuid=True), ForeignKey("partners.id"), nullable=False)

    partner = relationship("Partners", back_populates="documents")
