import uuid

from datetime import datetime
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, MappedAsDataclass
from sqlalchemy.sql import func

from . import Base


class TimestampMixin(MappedAsDataclass):
    __abstract__ = True  # Mark as abstract model

    created_at: Mapped[datetime] = mapped_column(default_factory=datetime.utcnow, nullable=False, init=False)
    updated_at: Mapped[datetime] = mapped_column(
        default_factory=datetime.utcnow,
        nullable=False,
        onupdate=func.current_timestamp().op("AT TIME ZONE")("UTC"),
        init=False,
    )


class Profile(TimestampMixin, Base):
    __tablename__ = "profiles"

    clerk_id: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    id: Mapped[str] = mapped_column(String(36), primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    seen_at: Mapped[datetime] = mapped_column(
        default_factory=datetime.utcnow,
        nullable=False,
        onupdate=func.current_timestamp().op("AT TIME ZONE")("UTC"),
        init=False,
    )

    def __repr__(self):
        return f"<Profile {self.id}/{self.clerk_id}>"
