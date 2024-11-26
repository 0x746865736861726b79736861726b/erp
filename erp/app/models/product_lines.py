import uuid

from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, UniqueConstraint, Numeric, ForeignKey

from app.models.base_model import Base


class ProductLines(Base):
    document_id = Column(UUID(as_uuid=True), ForeignKey("documents.id"), nullable=False)
    line_number = Column(Numeric, nullable=False)
    product_id = Column(UUID(as_uuid=True), ForeignKey("products.id"), nullable=False)
    quantity = Column(Numeric, nullable=False)
    price = Column(Numeric, nullable=False)
    total = Column(Numeric, nullable=False)

    document = relationship("Documents", back_populates="product_lines")
    product = relationship("Products", back_populates="product_lines")

    __table_args__ = (UniqueConstraint("document_id", "line_number"),)
