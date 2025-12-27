from sqlalchemy import Column, Integer, String, DateTime, func, UniqueConstraint
from src.database import Base

class Products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)

    __table_args__ = (
        UniqueConstraint("name", name="uq_products_name"),
    )