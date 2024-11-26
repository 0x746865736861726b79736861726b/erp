import uuid

from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, ForeignKey, CheckConstraint

from app.models.base_model import Base


class DocumentLinks(Base):
    parent_id = Column(UUID(as_uuid=True), ForeignKey("documents.id"), nullable=False)
    child_id = Column(UUID(as_uuid=True), ForeignKey("documents.id"), nullable=False)

    # links_type = Column(
    #     String,
    #     nullable=False,
    #     CheckConstraint("link_type IN ('parent-child', 'related', 'reference')"),
    # )

    parent = relationship("Documents", foreign_keys=[parent_id])
    child = relationship("Documents", foreign_keys=[child_id])
