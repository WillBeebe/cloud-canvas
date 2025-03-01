import uuid

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class APIToken(Base):
    __tablename__ = "api_tokens"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    token = Column(String, unique=True, index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user_references.id"))

    user = relationship("UserReference", back_populates="api_tokens")
